
import unittest
from . import main


class TestEditDistance(unittest.TestCase):

    def test_sample1(self):
        s1 = "PLEASANTLY"
        s2 = "MEANLY"
        actual = main.find_edit_distance(s1, s2)
        expected = 5
        self.assertEquals(actual, expected)


if __name__ == '__main__':
    unittest.main()
