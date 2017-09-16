
import unittest
from rosalind.common import util
from rosalind.bioinformatics.common import seqio
from . import main


class TestGenerateKmers(unittest.TestCase):

    def test_sample(self):
        self.run_test(5, "sample1.txt", "expected1.txt")

    def test_extra(self):
        self.run_test(100, "sample2.txt", "expected2.txt")

    def run_test(self, k, seq_name, expected_name):
        with open(util.find_file(seq_name, __file__), "r") as fp:
            fp.readline()   # skip count
            seq = fp.readline().strip()
        expected = seqio.read_list(expected_name, __file__)
        actual = main.generate_kmers(seq, k)
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
