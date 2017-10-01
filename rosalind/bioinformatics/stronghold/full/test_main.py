
import unittest
from . import main
from rosalind.common import util


class TestPeptideInference(unittest.TestCase):

    def test_sample1(self):
        expected = "KEKEP"
        self.run_test("sample1.txt", expected)

    def test_sample2(self):
        expected = "IHRVTIIGHIDDIMRPMTRIDAMCGEFGRDYSSMFWYTQDIATCDMKFSPASHAPMVYSIETSSYMTHRYNNYVQVKCVCDIMSYV" # noqa
        self.run_test("sample2.txt", expected)

    def run_test(self, fname, expected):
        L = []
        with open(util.find_file(fname, __file__), "r") as fp:
            for line in fp:
                L.append(float(line))
        actual = main.infer_peptide(L[0], L[1:])
        self.assertEquals(actual, expected)


if __name__ == '__main__':
    unittest.main()
