
def read(path):
    seqs = []
    names = []
    with open(path, "r") as fp:
        frag = ""
        for line in fp:
            line = line.strip()
            if line[:1] == '>':
                if len(frag) > 0:
                    seqs.append(frag)
                    frag = ""
                names.append(line[1:].strip())
            else:
                frag += line
        if len(frag) > 0:
            seqs.append(frag)

    return (seqs, names)
