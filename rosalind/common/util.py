
import sys
import os


def find_file(fname):
    # Does it exist in the current directory?
    if os.path.isfile(fname):
        return fname

    # Grab the directory containing the "main" module
    main_path = (os.path.abspath(sys.modules['__main__'].__file__))
    main_dir = os.path.dirname(main_path)
    path = os.path.join(main_dir, fname)

    if os.path.isfile(path):
        return path

    # Oops, couldn't find the file! Give up and bail!
    print "Could not find file '" + fname + "'."
    sys.exit(1)
