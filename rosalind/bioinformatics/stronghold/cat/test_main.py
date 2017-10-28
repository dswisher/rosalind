
import unittest
from . import main


class TestPerfectMatchings(unittest.TestCase):

    def test_sample1(self):
        self.run_test("AUAU", 2)

    def test_one(self):
        self.run_test("AUAUAUAUAU", 42)

    def test_two(self):
        self.run_test("AAAAAUUUUU", 1)

    def run_test(self, seq, expected):
        actual = main.count_matchings(seq)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
