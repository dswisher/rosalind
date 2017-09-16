
import unittest
from rosalind.bioinformatics.common import seqio
from . import main


class TestReconstructString(unittest.TestCase):

    def test_sample(self):
        self.run_test("sample1.txt", "expected1.txt")

    def test_extra(self):
        self.run_test("sample2.txt", "expected2.txt")

    def run_test(self, sample_name, expected_name):
        seqs = seqio.read_list(sample_name, __file__)
        expected = seqio.read_one(expected_name, __file__)
        actual = main.reconstruct_string(seqs)
        self.assertEquals(actual, expected)


if __name__ == '__main__':
    unittest.main()
