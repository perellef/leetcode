# https://leetcode.com/problems/longest-substring-without-repeating-characters/

s = ...

from collections import defaultdict

def løsning(s):

    indekser = defaultdict(list)

    m = 0
    start = 0
    for i,tegn in enumerate(s):
        if len(indekser[tegn]) == 1:
            m = max(m, i-start)
            for t in s[start: (start := indekser[tegn][0]+1)]:
                indekser[t].pop()
        indekser[tegn].append(i)
    return max(m, len(s)-start)

print(løsning(s))