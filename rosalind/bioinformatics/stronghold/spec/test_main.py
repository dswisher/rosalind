
import unittest
from rosalind.common import util
from . import main


class TestInferProtein(unittest.TestCase):

    def test_sample1(self):
        weights = [3524.8542, 3710.9335, 3841.974, 3970.0326, 4057.0646]
        protein = main.infer_protein(weights)
        self.assertEquals(protein, "WMQS")

    def test_sample2(self):
        weights = []
        with open(util.find_file("sample2.txt", __file__), "r") as fp:
            for line in fp:
                weights.append(float(line))
        expected = "NKKHNAARMINKKEVYEWDSPIDEPIMVCSVRYFNTQWIRGYKVMIKDKNNKFKAECGVPIHWIAFRDVTYSYVAHDQHCID" # noqa
        actual = main.infer_protein(weights)
        self.assertEquals(actual, expected)


if __name__ == '__main__':
    unittest.main()
