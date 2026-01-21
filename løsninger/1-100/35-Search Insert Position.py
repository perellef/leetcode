# https://leetcode.com/problems/search-insert-position/description/

nums = [1,3,5,6]
target = 7

def løsning(ns, target):
    nedre = 0
    øvre = len(ns)

    while True: 
        if nedre >= øvre:
            return øvre
        midt = nedre + (øvre-nedre)//2
    
        if ns[midt] < target:
            nedre = midt + 1
        elif ns[midt] > target:
            øvre = midt
        else:
            return midt

print(løsning(nums, target))