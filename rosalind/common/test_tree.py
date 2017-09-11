
import unittest
from .tree import Tree


class TestTree(unittest.TestCase):

    def test_construction(self):
        t = Tree('*', [Tree('1'),
                       Tree('2'),
                       Tree('+', [Tree('3'),
                                  Tree('4')])])
        print t


if __name__ == '__main__':
    unittest.main()
