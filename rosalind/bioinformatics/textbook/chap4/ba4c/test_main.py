
import unittest
from . import main
from rosalind.common import util


class TestSpectrum(unittest.TestCase):

    def test_sample1(self):
        protein = "LEQN"
        actual = main.generate_spectrum(protein)
        expected = [0, 113, 114, 128, 129, 227, 242, 242, 257, 355, 356, 370, 371, 484] # noqa
        self.assertItemsEqual(actual, expected)

    def test_sample2(self):
        protein = "IAQMLFYCKVATN"
        actual = main.generate_spectrum(protein)
        with open(util.find_file("expected2.txt", __file__), "r") as fp:
            expected = map(int, fp.readline().split())
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
