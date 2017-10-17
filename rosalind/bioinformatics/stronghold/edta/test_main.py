
import unittest
from . import main


class TestEditDistanceAlignment(unittest.TestCase):

    def test_sample1(self):
        s = "PRETTY"
        t = "PRTTEIN"
        actual = main.edit_distance_alignment(s, t)
        expected = (4, "PRETTY--", "PR-TTEIN")
        self.assertEquals(actual, expected)


if __name__ == '__main__':
    unittest.main()
