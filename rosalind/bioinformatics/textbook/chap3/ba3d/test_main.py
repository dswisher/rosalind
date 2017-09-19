
import unittest
from rosalind.common import util
from . import main


class TestGenerateKmers(unittest.TestCase):

    def test_sample(self):
        self.run_test("sample1.txt", "expected1.txt")

    def run_test(self, seq_name, expected_name):
        with open(util.find_file(seq_name, __file__), "r") as fp:
            k = int(fp.readline())
            seq = fp.readline().strip()
        expected = ["AAG -> AGA",
                    "TCT -> CTC,CTA",
                    "GAT -> ATT",
                    "AGA -> GAT",
                    "ATT -> TTC",
                    "CTA -> TAC",
                    "CTC -> TCT",
                    "TTC -> TCT"]
        actual = list(main.format_graph(main.build_graph(seq, k)))
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
