
import unittest
import math
from . import main


class TestSignedPermutations(unittest.TestCase):

    def test_2(self):
        perms = main.enumerate_signed_permutations(2)
        expected = [(-1, -2), (-1, 2), (1, -2), (1, 2),
                    (-2, -1), (-2, 1), (2, -1), (2, 1)]
        self.check_num(len(perms), 2)
        self.assertItemsEqual(perms, expected)

    def test_3(self):
        perms = main.enumerate_signed_permutations(3)
        expected = [(1, 2, 3), (-1, 2, 3), (1, -2, 3), (1, 2, -3), (-1, -2, 3), (-1, 2, -3), (1, -2, -3), (-1, -2, -3), # noqa
                    (1, 3, 2), (-1, 3, 2), (1, -3, 2), (1, 3, -2), (-1, -3, 2), (-1, 3, -2), (1, -3, -2), (-1, -3, -2), # noqa
                    (2, 1, 3), (-2, 1, 3), (2, -1, 3), (2, 1, -3), (-2, -1, 3), (-2, 1, -3), (2, -1, -3), (-2, -1, -3), # noqa
                    (2, 3, 1), (-2, 3, 1), (2, -3, 1), (2, 3, -1), (-2, -3, 1), (-2, 3, -1), (2, -3, -1), (-2, -3, -1), # noqa
                    (3, 1, 2), (-3, 1, 2), (3, -1, 2), (3, 1, -2), (-3, -1, 2), (-3, 1, -2), (3, -1, -2), (-3, -1, -2), # noqa
                    (3, 2, 1), (-3, 2, 1), (3, -2, 1), (3, 2, -1), (-3, -2, 1), (-3, 2, -1), (3, -2, -1), (-3, -2, -1)] # noqa
        self.check_num(len(perms), 3)
        self.assertItemsEqual(perms, expected)

    def permutations(self, n, k):
        return math.factorial(n) / math.factorial(n - k)

    def check_num(self, act, n):
        # Arrange n unsigned numbers
        a = self.permutations(n, n)

        # Arrange the negative signs
        b = math.pow(2, n)

        # The number of expected is the product
        self.assertEqual(act, a * b)


if __name__ == '__main__':
    unittest.main()
