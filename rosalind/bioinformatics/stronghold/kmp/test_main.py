
import unittest
from . import main


class TestTableBuilding(unittest.TestCase):

    def test_sample1(self):
        expected = [0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 3, 4, 5, 3, 0, 0]  # noqa
        self.run_test("CAGCATGGTATCACAGCAGAG", expected)

    def test_sample2(self):
        self.run_test("abababc", [0, 0, 1, 2, 3, 4, 0])

    def test_sample3(self):
        self.run_test("aaaaa", [0, 1, 2, 3, 4])

    def test_sample4(self):
        self.run_test("ababab", [0, 0, 1, 2, 3, 4])

    def test_sample5(self):
        self.run_test("abacabab", [0, 0, 1, 0, 1, 2, 3, 2])

    def test_sample6(self):
        self.run_test("aaabaaaaab", [0, 1, 2, 0, 1, 2, 3, 3, 3, 4])

    def test_sample7(self):
        self.run_test("abababca", [0, 0, 1, 2, 3, 4, 0, 1])

    def run_test(self, seq, expected):
        actual = main.build_table(seq)
        self.assertEquals(actual, expected)


if __name__ == '__main__':
    unittest.main()
