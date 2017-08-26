
import sys
import time

if len(sys.argv) < 2:
    print "You must specify the name of the file to load!"
    sys.exit(1)

with open(sys.argv[1], "r") as file:
    seq = file.readline().strip()
    nums = map(int, file.readline().strip().split())
    k = nums[0]
    L = nums[1]
    t = nums[2]

def pattern_count(seq, pat):
    count = 0
    plen = len(pat)
    for i in xrange(1 + len(seq) - plen):
        if seq[i:i + plen] == pat:
            count += 1
    return count

def frequent_words(seq, k, t):
    freq = set()
    count = []
    for i in xrange(len(seq) - k):
        pat = seq[i:i+k]
        count.append(pattern_count(seq, pat))
    max_count = max(count)
    if max_count >= t:
        for i in xrange(len(seq) - k):
            if count[i] == max_count:
                freq.add(seq[i:i+k])
    return sorted(freq)

def find_clumps(seq, k, L, t):
    clumps = set()
    for i in xrange(1 + len(seq) - L):
        new = frequent_words(seq[i:i+L], k, t)
        for c in new:
            clumps.add(c)
    return sorted(clumps)

start_time = time.time()
print " ".join(find_clumps(seq, k, L, t))
print("--- %s seconds ---" % (time.time() - start_time))

