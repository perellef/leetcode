# https://leetcode.com/problems/group-anagrams/description/

strs = ["eat","tea","tan","ate","nat","bat"]

from collections import defaultdict

def løsning(strs):
    grupper = defaultdict(list)
    for s in strs:
        grupper[tuple(sorted(s))].append(s)
    return list(grupper.values())

print(løsning(strs))