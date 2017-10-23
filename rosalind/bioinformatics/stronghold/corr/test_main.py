
import unittest
from rosalind.common import util
from rosalind.bioinformatics.common import fasta
from rosalind.bioinformatics.common import seqio
from . import main


class TestErrorCorrection(unittest.TestCase):

    def test_sample1(self):
        self.run_test("sample1.txt", "expected1.txt")

    def run_test(self, sample_name, expected_name):
        seqs, _ = fasta.read(util.find_file(sample_name, __file__))
        expected = seqio.read_list(util.find_file(expected_name, __file__))
        actual = main.find_corrections(seqs)

        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
