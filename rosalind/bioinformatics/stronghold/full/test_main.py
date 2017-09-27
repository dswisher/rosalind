
import unittest
from . import main


class TestPeptideInference(unittest.TestCase):

    def test_sample1(self):
        L = [1988.21104821, 610.391039105, 738.485999105,
             766.492149105, 863.544909105, 867.528589105,
             992.587499105, 995.623549105, 1120.6824591,
             1124.6661391, 1221.7188991, 1249.7250491, 1377.8200091]
        actual = main.infer_peptide(L[0], L[1:])
        expected = "KEKEP"
        self.assertEquals(actual, expected)


if __name__ == '__main__':
    unittest.main()
