# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

nums = [0,0,1,1,1,2,2,3,3,4]

def løsning(nums):
    k = 1
    for i in range(len(nums)-1,0,-1):
        if nums[i] == nums[i-1]:
            nums.pop(i)
        else:
            k += 1
    return k

print(løsning(nums))