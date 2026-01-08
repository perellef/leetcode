# https://leetcode.com/problems/sort-colors/

nums = [1,1,0,1,2,2,0,0]

def løsning(nums):
    nhash = {0: [], 1: [], 2:[]}
    for i,n in enumerate(nums):
        nhash[n].append(i)

    for i in range(min(len(nhash[0]), len(nhash[2]))):
        i0 = nhash[0][len(nhash[0])-1-i] 
        i2 = nhash[2][i]
        if i0 < i2:
            break

        nums[i0], nums[i2] = nums[i2], nums[i0]
    
    nhash = {0: [], 1: [], 2:[]}
    for i,n in enumerate(nums):
        nhash[n].append(i)

    for i in range(min(len(nhash[1]), len(nhash[2]))):
        i1 = nhash[1][len(nhash[1])-1-i] 
        i2 = nhash[2][i]
        if i1 < i2:
            break

        nums[i1], nums[i2] = nums[i2], nums[i1]

    nhash = {0: [], 1: [], 2:[]}
    for i,n in enumerate(nums):
        nhash[n].append(i)

    for i in range(min(len(nhash[1]), len(nhash[0]))):
        i0 = nhash[0][len(nhash[0])-1-i] 
        i1 = nhash[1][i]
        if i0 < i1:
            break

        nums[i0], nums[i1] = nums[i1], nums[i0]
    
    print(nums)
    
løsning(nums)