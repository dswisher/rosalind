
import unittest
from . import main


class TestProb(unittest.TestCase):

    def test_sample1(self):
        seq = "ACGATACAA"
        gcContent = [0.129, 0.287, 0.423, 0.476, 0.641, 0.742, 0.783]
        actual = main.compute_prob(seq, gcContent)
        expected = [-5.737, -5.217, -5.263, -5.360, -5.958, -6.628, -7.009]
        self.assertEqual(len(actual), len(expected))
        for i in xrange(len(actual)):
            self.assertAlmostEqual(actual[i], expected[i], places=3)


if __name__ == '__main__':
    unittest.main()
