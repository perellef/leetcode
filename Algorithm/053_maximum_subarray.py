# https://leetcode.com/problems/maximum-subarray/description/

nums = [1,2]

def løsning(ns):

    sum = ns[-1]
    for i in range(len(nums)):
        
        if i+1 == len(nums) or ns[i] < 0 or ns[i] + ns[i+1] < 0:
            sum = max(sum, ns[i])
            continue
        
        ns[i+1] = ns[i] + ns[i+1]
        sum = max(sum, ns[i])

    return max(0, sum)
    
print(løsning(nums))