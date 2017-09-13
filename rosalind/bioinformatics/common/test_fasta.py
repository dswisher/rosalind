
import unittest
import tempfile
import os
from . import fasta


class TestFasta(unittest.TestCase):

    def test_simple(self):
        lines = ["> Sequence 1", "AGCTAGCTAGCT"]
        path = self.make_temp(lines)
        seqs, names = fasta.read(path)
        self.assertItemsEqual(seqs, ["AGCTAGCTAGCT"])
        self.assertItemsEqual(names, ["Sequence 1"])
        self.cleanup(path)

    def make_temp(self, lines):
        fd, path = tempfile.mkstemp()
        with open(path, 'w') as fp:
            for l in lines:
                fp.write(l + '\n')
        os.close(fd)
        return path

    def cleanup(self, path):
        os.remove(path)


if __name__ == '__main__':
    unittest.main()
