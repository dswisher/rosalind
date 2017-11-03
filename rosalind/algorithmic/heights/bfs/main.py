
import sys
from rosalind.common import util
from rosalind.bioinformatics.common import debruijn


# noqa From: http://interactivepython.org/courselib/static/pythonds/BasicDS/ImplementingaQueueinPython.html
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def do_bfs(node, dist):
    q = Queue()
    q.enqueue((node, 0))
    while not q.isEmpty():
        n, d = q.dequeue()
        for e in n.out_edges:
            tail = int(e.tail.label) - 1
            if dist[tail] == -1:    # not yet visited
                dist[tail] = d + 1
                q.enqueue((e.tail, d + 1))


def main(fname):
    # Read in the graph
    with open(util.find_file(fname), "r") as fp:
        node_dict = debruijn.read_edge_list(fp)

    # List of distances to each node
    dist = [-1 for i in node_dict.values()]
    dist[0] = 0

    # Set up a queue of all nodes
    do_bfs(node_dict['1'], dist)

    # Print the result
    print " ".join(map(str, dist))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Please enter the name of the data file!"
        sys.exit(1)
    main(sys.argv[1])
