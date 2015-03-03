import os

__all__ = ['get_home']

def get_home():
    # This function should be robust
    # First, let us try with expanduser
    try:
        homedir = os.path.expanduser("~")
    except ImportError:
        # This may happen.
        pass
    else:
        if os.path.isdir(homedir):
            return homedir
    # Then, with getenv
    for this in ('HOME', 'USERPROFILE', 'TMP'):
        # getenv is same as os.environ.get
        homedir = os.environ.get(this)
        if homedir is not None and os.path.isdir(homedir):
            return homedir
    return None
