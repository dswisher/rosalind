
import unittest
from . import main


class TestRandomMotifs(unittest.TestCase):

    def test_sample1(self):
        N = 90000
        x = 0.6
        dna = "ATAGCCGA"
        actual = main.compute_probability(N, x, dna)
        expected = 0.689
        self.assertAlmostEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
