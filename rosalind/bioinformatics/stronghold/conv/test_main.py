
import unittest
from . import main


class TestSpectralConvolution(unittest.TestCase):

    def test_sample1(self):
        s1 = [186.07931, 287.12699, 548.20532, 580.18077, 681.22845, 706.27446, 782.27613, 968.35544, 968.35544]    # noqa
        s2 = [101.04768, 158.06914, 202.09536, 318.09979, 419.14747, 463.17369]
        num, big = main.convolve(s1, s2)
        self.assertEquals(num, 3)
        self.assertEquals(big, 85.03163)


if __name__ == '__main__':
    unittest.main()
