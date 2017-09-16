
import unittest
from rosalind.common import util
from . import main


class TestReconstructString(unittest.TestCase):

    def test_sample1(self):
        self.run_test("sample1.txt", "expected1.txt")

    # TODO - enable if performance is ever improved
    # def test_sample2(self):
    #     self.run_test("sample2.txt", "expected2.txt")

    def test_sample3(self):
        self.run_test("sample3.txt", "expected3.txt")

    def run_test(self, sample_name, expected_name):
        seqs = []
        with open(util.find_file(sample_name, __file__), "r") as fp:
            for line in fp:
                seqs.append(line.strip())

        expected = []
        with open(util.find_file(expected_name, __file__), "r") as fp:
            for line in fp:
                bits = line.strip().split()
                expected.append((bits[0], bits[2]))

        actual = main.build_overlap_graph(seqs)
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
