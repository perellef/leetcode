# https://leetcode.com/problems/unique-paths/

from math import factorial

m = 7
n = 3
def løsning(m,n):
    return int(factorial(m+n-2)/(factorial(m-1)*factorial(n-1)))

print(løsning(m,n))