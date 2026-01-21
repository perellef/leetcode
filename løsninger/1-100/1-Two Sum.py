# https://leetcode.com/problems/two-sum/

nums = ...
target = ...

def løsning(nums, target):
    numap = {n: i for i,n in enumerate(nums)}
    for i,n in enumerate(nums):
        if target - n in numap:
            if i == numap[target-n]:
                continue
            return [i, numap[target-n]]
        
print(løsning(nums, target))