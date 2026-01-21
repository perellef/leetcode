# https://leetcode.com/problems/first-missing-positive/

nums = [1,2,0]

def løsning(nums):
    numset = set(nums)

    i = 1
    while True:
        if i not in numset:
            return i
        i += 1
print(løsning(nums))