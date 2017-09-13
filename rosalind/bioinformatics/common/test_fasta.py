
import unittest
import tempfile
import os
from . import fasta


class TestFasta(unittest.TestCase):

    def test_simple(self):
        lines = ["> Sequence 1", "AGCTAGCTAGCT", "> Sequence 2", "AAAA"]
        self.path = self.make_temp(lines)
        seqs, names = fasta.read(self.path)
        self.assertItemsEqual(seqs, ["AGCTAGCTAGCT", "AAAA"])
        self.assertItemsEqual(names, ["Sequence 1", "Sequence 2"])

    def test_continuation(self):
        lines = ["> Sequence 1", "AAAA", "CCCC", "> Sequence 2", "TTTT"]
        self.path = self.make_temp(lines)
        seqs, names = fasta.read(self.path)
        self.assertItemsEqual(seqs, ["AAAACCCC", "TTTT"])
        self.assertItemsEqual(names, ["Sequence 1", "Sequence 2"])

    def make_temp(self, lines):
        fd, path = tempfile.mkstemp()
        with open(path, 'w') as fp:
            for l in lines:
                fp.write(l + '\n')
        os.close(fd)
        return path

    def tearDown(self):
        os.remove(self.path)


if __name__ == '__main__':
    unittest.main()
