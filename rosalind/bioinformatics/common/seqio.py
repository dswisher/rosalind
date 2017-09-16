
from rosalind.common import util


def read_one(fname, extra_path=None):
    with open(util.find_file(fname, extra_path), "r") as fp:
        return fp.readline().strip()


def read_list(fname, extra_path=None):
    seqs = []
    with open(util.find_file(fname, extra_path), "r") as fp:
        for line in fp:
            seqs.append(line.strip())
    return seqs
