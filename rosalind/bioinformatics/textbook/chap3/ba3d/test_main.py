
import unittest
from rosalind.common import util
from . import main


class TestGenerateKmers(unittest.TestCase):

    def test_sample1(self):
        self.run_test("sample1.txt", "expected1.txt")

    def test_sample2(self):
        self.run_test("sample2.txt", "expected2.txt")

    def run_test(self, seq_name, expected_name):
        with open(util.find_file(seq_name, __file__), "r") as fp:
            k = int(fp.readline())
            seq = fp.readline().strip()
        with open(util.find_file(expected_name, __file__), "r") as fp:
            expected = fp.read().splitlines()
        actual = list(main.format_graph(main.build_graph(seq, k)))
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
