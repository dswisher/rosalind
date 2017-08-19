
import sys

if len(sys.argv) != 4:
    print "Usage: python iprb.py k m n"
    sys.exit(1)

k = int(sys.argv[1])
m = int(sys.argv[2])
n = int(sys.argv[3])


def get_prob(k, m, n):
    dom1dom2 = k * (k - 1) * 1.0    # AA + AA
    dom1het2 = k * m * 1.0          # AA + Aa
    dom1rec2 = k * n * 1.0          # AA + aa
    dom1 = dom1dom2 + dom1het2 + dom1rec2

    het1dom2 = m * k * 1.0          # Aa + AA
    het1het2 = m * (m - 1) * 0.75   # Aa + Aa
    het1rec2 = m * n * 0.5          # Aa + aa
    het1 = het1dom2 + het1het2 + het1rec2

    rec1dom2 = n * k * 1.0          # aa + AA
    rec1het2 = n * m * 0.5          # aa + Aa
    rec1rec2 = n * (n - 1) * 0.0    # aa + aa
    rec1 = rec1dom2 + rec1het2 + rec1rec2

    return (dom1 + het1 + rec1) / (k + m + n) / (k + m + n - 1)

print round(get_prob(k, m, n), 5)

