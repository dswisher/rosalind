
import sys
from Bio.Seq import Seq


def main(fname):
    with open(fname, "r") as fp:
        sample = fp.readline().strip()

    my_seq = Seq(sample)
    a = my_seq.count("A")
    c = my_seq.count("C")
    g = my_seq.count("G")
    t = my_seq.count("T")

    print a, c, g, t


if len(sys.argv) < 2:
    print("You must enter the name of the file to load!")
    sys.exit(1)

fname = sys.argv[1]
main(fname)
