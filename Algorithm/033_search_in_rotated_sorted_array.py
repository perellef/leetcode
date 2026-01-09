# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

nums = [3,5,1]
target = 5

def finn_rotasjon(nums):
    if len(nums) == 1:
        return 0
    
    nedre = 0
    øvre = len(nums)-1
    while True:
        midt = nedre + (øvre-nedre)//2
        if nums[midt] > nums[midt+1]:
            return midt+1
        if øvre==nedre:
            return 0

        if nums[midt] < nums[øvre]:
            øvre = midt
        elif  nums[midt] > nums[øvre]:
            nedre = midt

def løsning(nums, target):
    rotasjon = finn_rotasjon(nums)

    nedre = 0
    øvre = len(nums)-1
    while øvre-nedre >= 0:

        midt = nedre + (øvre-nedre)//2
        i = (midt + rotasjon) % len(nums)

        if nums[i] > target:
            øvre = midt - 1
        elif nums[i] < target:
            nedre = midt + 1
        else:
            return i
    return -1
    


print(løsning(nums, target))