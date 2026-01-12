# https://leetcode.com/problems/combination-sum-ii/

candidates = [1,1,1,1,1,1,2,3,5]
target = 6

from collections import defaultdict
def løsning(ns, target):
    n_hash = defaultdict(int)
    for n in ns:
        n_hash[n] += 1

    nøkler = list(n_hash)

    def _rek_(i, lst, s):
        if s == target:
            return [lst]
        if s > target or i == len(nøkler):
            return []
        
        ny_lst = []
        for k in range(0,n_hash[nøkler[i]]+1):
            for e in _rek_(i+1, lst+[k], s+k*nøkler[i]):
                ny_lst.append(e)
        return ny_lst

    l = _rek_(0, [], 0)

    løsninger = []
    for el in l:
        løsning = []
        for i,v in enumerate(el):
             løsning += v*[nøkler[i]]
        løsninger.append(løsning)

    return løsninger

print(løsning(candidates, target))