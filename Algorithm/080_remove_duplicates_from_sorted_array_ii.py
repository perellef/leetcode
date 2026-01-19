# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

nums = [1,2,2,2,3,4,4,5]

def løsning(ns):
    forrige = None
    antall = 0
    for i in range(len(ns)-1,-1,-1):
        if ns[i] == forrige and antall == 2:
            ns.pop(i)
            continue
        if ns[i] != forrige:
            antall = 0
            
        forrige = ns[i]
        antall += 1
    
    print(ns)

print(løsning(nums))