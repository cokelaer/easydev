import os


__all__ = ["LSFCluster"]


class LSFCluster(object):
    """Simple class to create jobs for LSF cluster with a common jobs to run all
    of them.

    ::

        l = LSFCluster()
        l.add_cmd("preprocessing --input test.dat --output test2.dat", level=1)
        l.add_cmd("postprocessing --input test2.dat", level=2)
        l.create_scripts()

    create jobs taking care of the dependencies between commands. 
    commands in level 2 waits for those in level 1 to be over.

    """
    def __init__(self, prog, tag="generic", verbose=False):
        self.reset()
        self.prog = prog
        self.tag = tag
        self.error = ""
        self.output = ""
        self.verbose = verbose

    def reset(self):
        """remove joves and results"""
        self.jobs = [] # a list of processes
        self.levels = []
        self.filenames = {}
        self.script_filename = None

    def add_cmd(self, cmd, level=1):
        """add a job in the pool


        :param str cmd: command to run
        :param int level: dependency level. Lower level must be run first.
        """
        if self.verbose:
            print("Adding jobs in the queue.. (%s)\n" % cmd)
        self.jobs.append(cmd)
        #todo: sanity checks of the layer values?
        self.levels.append(level)

    def create_scripts(self):
        """Create a script for each individual command and a main script"""
        # create individual scripts
        for i, j in enumerate(self.jobs):
            self._bsub(j, Id=i)

        # create main script
        self.script_filename  = "runme_%s.sh" % self.tag
        f = open(self.script_filename, "w")
        f.write("""#!/bin/bash\n""")
        f.write("""# do not edit. Automatically created by %s (revision $Rev: 2007 $)\n""" % self.prog)
        for id_, filename in self.filenames.items():
            f.write("""bsub -q research-rh6 %s -e lsf_jobs_%s.err -o lsf_jobs_%s.out\n""" % (filename, id_, id_))
        f.close()
        os.system("chmod 755 %s" % self.script_filename)
        if self.verbose:
            print("type: sh %s  ; make sure to have used chmod 755 before" % self.script_filename)

    def _bsub(self, cmd, Id=None):
        """Create the LSF command."""
        filename = "lsf_jobs_%s_%s.sh" % (Id, self.tag)
        self.filenames[Id] = filename
        f = open(filename, "w")
        f.write("""#!/bin/bash\n""")
        f.write("""# do not edit. Automatically create by %s (revision $Rev: 2007 $)\n""" % self.prog)
        f.write("""%s\n""" % cmd)
        f.close()
        os.system("chmod 755 %s" % filename)

    def cleanup(self):
        """Remove the files that have been created"""
        for f in self.filenames.values():
            os.remove(f)
        os.remove(self.script_filename)
