
import unittest
from rosalind.common import util
from . import main


class TestReconstructString(unittest.TestCase):

    def test_sample(self):
        self.run_test("sample1.txt", "expected1.txt")

    def test_extra(self):
        self.run_test("sample2.txt", "expected2.txt")

    def run_test(self, sample_name, expected_name):
        seqs = []
        with open(util.find_file(sample_name, __file__), "r") as fp:
            for line in fp:
                seqs.append(line.strip())

        with open(util.find_file(expected_name, __file__), "r") as fp:
            expected = fp.readline().strip()

        actual = main.reconstruct_string(seqs)
        self.assertEquals(actual, expected)


if __name__ == '__main__':
    unittest.main()
