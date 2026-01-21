# https://leetcode.com/problems/jump-game/description/

nums = [3,2,1,0,4]

def løsning(ns):
    j = len(ns)-1
    for i in range(len(ns)-2,-1,-1):
        if ns[i] >= j-i:
            j = i
    return j == 0

print(løsning(nums))