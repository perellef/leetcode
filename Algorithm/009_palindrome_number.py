# https://leetcode.com/problems/palindrome-number/

x = 121

def løsning(x):
    s = str(x)
    for i in range(len(s)//2+1):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

print(løsning(x)) 