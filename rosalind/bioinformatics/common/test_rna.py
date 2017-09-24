
import unittest
from . import rna


class TestRna(unittest.TestCase):

    def test_sample1(self):
        seq = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
        actual = rna.translate(seq)
        expected = "MAMAPRTEINSTRING"
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
