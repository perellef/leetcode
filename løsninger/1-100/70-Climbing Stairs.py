# https://leetcode.com/problems/climbing-stairs/

n = 3

import math

def løsning(n):
    s = 0
    for step in range(0,n+1,2):
        dobbeltsteg = step//2
        enkeltsteg = n-step

        s += math.factorial(enkeltsteg+dobbeltsteg)//(math.factorial(enkeltsteg)*math.factorial(dobbeltsteg))
    return s
print(løsning(n))