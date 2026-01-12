# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

nums = [0,0,1,1,1,2,2,3,3,3,4,4,4,4,5,5,6,6,6,8,10,10]
target = 4

def løsning(ns, target):
    nedre_nedre = 0
    nedre_øvre = len(ns)-1
    øvre_nedre = 0
    øvre_øvre = len(ns)-1

    while True: 
        if øvre_øvre < nedre_nedre:
            return [-1, -1]

        if nedre_øvre - nedre_nedre >= 0:
            midt = nedre_nedre + (nedre_øvre-nedre_øvre)//2
        elif øvre_øvre - øvre_nedre >= 0:
            midt = øvre_nedre + (øvre_øvre-øvre_nedre)//2
        else:
            break
    
        if ns[midt] < target:
            nedre_nedre = midt + 1
        elif ns[midt] > target:
            øvre_øvre = midt - 1
        else:
            nedre_øvre = min(nedre_øvre, midt-1)
            øvre_nedre = max(øvre_nedre, midt+1)

    return nedre_øvre+1,øvre_nedre-1

print(løsning(nums, target))