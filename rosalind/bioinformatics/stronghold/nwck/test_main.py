
import unittest
from . import main


class TestErrorCorrection(unittest.TestCase):

    def test_sampleA(self):
        tree = "(cat)dog;"
        node1 = "dog"
        node2 = "cat"
        dist = main.find_distance(tree, node1, node2)
        self.assertEquals(dist, 1)

    # TODO - add second sample test


if __name__ == '__main__':
    unittest.main()
