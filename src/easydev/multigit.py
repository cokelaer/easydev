import glob
import sys
import os
from easydev.console import red, green

def multigit(args):
    """Simple utility to apply a git command to all local directories"""
    if len(args) == 0:
        return
    else:
        command = args[0]

    directories = glob.glob('*')
    directories = [x for x in directories if os.path.isdir(x)]
   
    failed = []
    for directory in directories:
        print("Entering in {0}".format(directory))
        code = "cd {0}; git {1}".format(directory, command)
        try:
            print(code)
            status = os.system(code)
            if status == 0:
                print(green('ok'))
            else:
                raise Error
        except:
            failed.append(directory)
            print(red("Failed. Skipped"))
        finally:
            code = "cd .."
            os.system(code)

    print    

if __name__ == "__main__":    
    args = sys.argv[1:]  # 1 ignore the name of the calling program itself

    if len(args)==0:
        print(red("USAGE: python multigit.py pull"))
    else:
        multigit(args)




