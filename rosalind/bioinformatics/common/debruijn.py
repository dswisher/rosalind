
class Node:
    """ Node in the graph """
    def __init__(self, lab):
        self.label = lab
        self.out_edges = []
        self.in_edges = []

    def add_out(self, e):
        self.out_edges.append(e)

    def add_in(self, e):
        self.in_edges.append(e)

    def __repr__(self):
        return self.label


class Edge:
    """ Edge in the graph """
    def __init__(self, lab, head, tail):
        self.label = lab
        self.head = head
        self.tail = tail

    def __repr__(self):
        return self.label


def create_graph(seqs):
    nodes = {}

    k = len(seqs[0]) - 1

    for s in seqs:
        prefix = s[:k]
        suffix = s[-k:]

        if prefix in nodes.keys():
            n1 = nodes[prefix]
        else:
            n1 = Node(prefix)
            nodes[prefix] = n1

        if suffix in nodes.keys():
            n2 = nodes[suffix]
        else:
            n2 = Node(suffix)
            nodes[suffix] = n2

        edge = Edge(s, n1, n2)

        n1.add_out(edge)
        n2.add_in(edge)

    return nodes


def format_graph(graph):
    for n in graph.values():
        l = n.label
        r = []
        for e in n.out_edges:
            r.append(e.tail.label)
        if len(r) > 0:
            yield l + " -> " + ",".join(sorted(r))


def read_adjacency_list(fp):
    # TODO
    return create_graph(["ACTG", "CTGA", "TGAC"])
