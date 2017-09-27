
import unittest
from . import masses


class TestPeptideInference(unittest.TestCase):

    def test_get_mass(self):
        self.assertEquals(masses.get_mass('W'), 186.07931)

    def test_get_amino_acid(self):
        self.assertEquals(masses.get_amino_acid(186), 'W')
