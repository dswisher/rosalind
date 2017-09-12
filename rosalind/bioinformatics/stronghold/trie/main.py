
import sys
from rosalind.common import util


def read_data(fname):
    dna = []
    with open(fname, "r") as fp:
        for line in fp:
            dna.append(line.strip())
    return dna


_id = '_id_'


def add_to_adj(adj, node):
    fr = node[_id]
    for k, v in node.items():
        if k != _id:
            to = v[_id]
            adj.append([fr, to, k])
            add_to_adj(adj, v)


def get_adjacency(trie):
    adj = []
    add_to_adj(adj, trie)
    return adj


# A trie as a dict of dicts; the _id key holds a unique ID for the node
def make_trie(dna):
    num = 1
    root = dict()
    root[_id] = num
    for seq in dna:
        node = root
        for n in seq:
            if n in node:
                node = node[n]
            else:
                node[n] = dict()
                node = node[n]
                num += 1
                node[_id] = num
    return root


def main(fname):
    dna = read_data(util.find_file(fname))
    trie = make_trie(dna)
    adj = get_adjacency(trie)
    for item in adj:
        print " ".join(map(str, item))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "You must specify the name of the data file to load!"
        sys.exit(1)
    main(sys.argv[1])
