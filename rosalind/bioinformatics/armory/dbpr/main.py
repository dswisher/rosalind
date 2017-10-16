import sys
from Bio import ExPASy
from Bio import SwissProt


def main(id):
    handle = ExPASy.get_sprot_raw(id)
    record = SwissProt.read(handle)
    for cr in record.cross_references:
        if cr[0] == "GO":
            bits = cr[2].split(":")
            if bits[0] == "P":
                print bits[1]


if len(sys.argv) < 2:
    print("You must enter the protein ID!")
    sys.exit(1)

id = sys.argv[1]
main(id)
