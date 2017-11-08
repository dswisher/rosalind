
import unittest
from . import main


class TestReversalDistance(unittest.TestCase):

    def test1(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        b = [3, 1, 5, 2, 7, 4, 9, 6, 10, 8]
        self.assertEqual(main.reversal_distance(a, b), 9)


if __name__ == '__main__':
    unittest.main()
