from easydev import SmartFormatter
import argparse



class Options(argparse.ArgumentParser):
    def  __init__(self, prog="test"):
        usage = """standalone test"""
        description="""blabla"""
        super(Options, self).__init__(usage=usage, prog=prog,
              description=description, formatter_class=SmartFormatter)
        self.add_argument("--config-params", dest="config_params",
            type=str,
            help="""FORMAT|Overwrite any field in the config file by using
the following convention. A config file is in YAML format
and has a hierarchy of parametesr. For example:

    samples:
        file1: R1.fastq.gz
        file2: R2.fastq.gz
    bwa_mem_phix:
        mem:
            threads: 2
        """)


def test():
    options = Options()
    try:
        options.parse_args(["--help"])
    except:
        pass
