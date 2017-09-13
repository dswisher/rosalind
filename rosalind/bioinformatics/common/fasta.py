
def read(path):
    seqs = []
    names = []
    with open(path, "r") as fp:
        for line in fp:
            line = line.strip()
            # TODO - handle continuations!
            if line[:1] == '>':
                names.append(line[1:].strip())
            else:
                seqs.append(line)

    return (seqs, names)
