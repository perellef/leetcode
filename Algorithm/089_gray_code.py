# https://leetcode.com/problems/gray-code/

n = 3

def løsning(n):
    løsninger = {1: ["0","1"]}

    for k in range(2,n+1):
        løsninger[k] = ["0"+e  for e in løsninger[k-1]]+["1"+e for e in reversed(løsninger[k-1])]

    return [int(e,2) for e in løsninger[n]]

print(løsning(n))