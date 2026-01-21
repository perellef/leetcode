# https://leetcode.com/problems/subsets-ii/

nums = [1,2,2]

from collections import defaultdict

def løsning(nums):
    nhash = defaultdict(int)
    for n in nums:
        nhash[n] += 1

    nøkler = list(nhash)

    def _rek_(sublists, i):
        if i == len(nøkler):
            return sublists
        
        ny_sublist = []
        for sublist in sublists:
            for antall in range(nhash[nøkler[i]]+1):
                ny_sublist.append(sublist+antall*[nøkler[i]])

        return _rek_(ny_sublist, i+1)

    return _rek_([[]], 0)

print(løsning(nums))