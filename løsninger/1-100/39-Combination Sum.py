# https://leetcode.com/problems/combination-sum/

candidates = [2,3,6,7]
target = 7

from collections import defaultdict
def løsning(ns, target):
    
    n_hash = defaultdict(list)
    n_hash[0] = []
    
    target_trær = []
    while True:
        ny_n_hash = defaultdict(list)
        for n in ns:
            for k,v in n_hash.items():
                if n+k > target:
                    continue
                elif n+k == target:
                    target_trær.append((n,v))
                else:
                    ny_n_hash[n+k].append((n,v))
        if len(ny_n_hash) == 0:
            break
        n_hash = ny_n_hash
    
    def _rek_(tre, maks):
        n,indre_tre = tre
        if indre_tre == []:
            if maks < n:
                return []
            return [[n]]

        lst = []
        for gren in indre_tre:
            if n > maks:
                continue
            for e in _rek_(gren, n):
                if e != []:
                    lst.append([n]+e)
        return lst
    
    l = []
    for tre in target_trær:
        l.extend(_rek_(tre, target))
    return l

print(løsning(candidates, target))