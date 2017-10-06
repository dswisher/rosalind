
import unittest
from . import main


class TestSpectrum(unittest.TestCase):

    def test_sample1(self):
        protein = "LEQN"
        actual = main.generate_spectrum(protein)
        expected = [0, 113, 114, 128, 129, 227, 242, 242, 257, 355, 356, 370, 371, 484] # noqa
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
