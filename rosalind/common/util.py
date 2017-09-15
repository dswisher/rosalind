
import sys
import os


def find_file(fname, extra_root=None):
    # Does it exist in the current directory?
    if os.path.isfile(fname):
        return fname

    # If extra root is specified, look in its directory
    if extra_root is not None:
        work_dir = os.path.dirname(extra_root)
        path = os.path.join(work_dir, fname)

        if os.path.isfile(path):
            return path

    # Grab the directory containing the "main" module
    work_path = (os.path.abspath(sys.modules['__main__'].__file__))
    work_dir = os.path.dirname(work_path)
    path = os.path.join(work_dir, fname)

    if os.path.isfile(path):
        return path

    # Oops, couldn't find the file! Give up and bail!
    print "Could not find file '" + fname + "'."
    sys.exit(1)
