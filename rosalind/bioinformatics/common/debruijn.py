
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
        head.add_out(self)
        tail.add_in(self)

    def __repr__(self):
        return self.label


def _find_or_add_node(col, name):
    if name in col.keys():
        node = col[name]
    else:
        node = Node(name)
        col[name] = node
    return node


def create_graph(seqs):
    nodes = {}

    k = len(seqs[0]) - 1

    for s in seqs:
        prefix = s[:k]
        suffix = s[-k:]

        n1 = _find_or_add_node(nodes, prefix)
        n2 = _find_or_add_node(nodes, suffix)

        Edge(s, n1, n2)
    return nodes


def format_graph(graph):
    for n in graph.values():
        l = n.label
        r = []
        for e in n.out_edges:
            r.append(e.tail.label)
        if len(r) > 0:
            yield l + " -> " + ",".join(sorted(r))


def format_adjacency(graph):
    for n in graph.values():
        for e in n.out_edges:
            yield "(" + e.head.label + ", " + e.tail.label + ")"


def read_adjacency_list(fp):
    nodes = {}
    for line in fp:
        line = line.strip()
        bits = line.split()
        if len(bits) != 3:
            raise ValueError("Line '" + line + "' is not well formed.")
        head = _find_or_add_node(nodes, bits[0])
        for t in bits[2].split(','):
            tail = _find_or_add_node(nodes, t)
            label = head.label + " -> " + tail.label
            Edge(label, head, tail)
    return nodes
