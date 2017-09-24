
import unittest
from rosalind.common import util
from rosalind.bioinformatics.common import debruijn
from . import main


class TestGenerateKmers(unittest.TestCase):

    def test_sample1(self):
        self.run_test("sample1.txt", "expected1.txt")

    def run_test(self, sample_name, expected_name):
        with open(util.find_file(sample_name, __file__), "r") as fp:
            graph = debruijn.read_adjacency_list(fp)
        with open(util.find_file(expected_name, __file__), "r") as fp:
            expected = fp.readline().strip()
        cycle = main.find_eulerian_cycle(graph)
        actual = main.format_path(cycle)
        duped = actual + actual[actual.find("-"):]
        self.assertEqual(len(actual), len(expected))
        self.assertTrue(duped.find(expected) != -1)

    def cycle_to_string(self, cycle):
        str = ""
        for n in cycle:
            str += n.label + "-"
        return str


if __name__ == '__main__':
    unittest.main()
