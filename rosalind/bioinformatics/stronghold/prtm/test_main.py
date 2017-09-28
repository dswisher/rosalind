
import unittest
from . import main


class TestProteinMass(unittest.TestCase):

    def test_sample1(self):
        protein = "SKADYEK"
        actual = main.calc_mass(protein)
        self.assertAlmostEqual(actual, 821.392, places=3)


if __name__ == '__main__':
    unittest.main()
