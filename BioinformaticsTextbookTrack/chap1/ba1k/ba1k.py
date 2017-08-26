
import sys

if len(sys.argv) != 2:
    print "Please provide the name of the file to load!"
    sys.exit(1)


def symbol_to_number(s):
    return { 'A': 0, 'C': 1, 'G': 2, 'T': 3 }[s]


def pattern_to_number(pat):
    if len(pat) == 0:
        return 0
    symbol = pat[-1:]
    prefix = pat[:-1]
    return 4 * pattern_to_number(prefix) + symbol_to_number(symbol)


def computing_frequencies(text, k):
    frequency_array = [0] * pow(4, k)

    for i in xrange(0, 1 + len(text) - k):
        pattern = text[i:i+k]
        j = pattern_to_number(pattern)
        frequency_array[j] += 1

    return frequency_array


with open(sys.argv[1], "r") as file:
    seq = file.readline().strip()
    k = int(file.readline())


print " ".join(map(str, computing_frequencies(seq, k)))

