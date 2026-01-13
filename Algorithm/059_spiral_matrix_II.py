# https://leetcode.com/problems/spiral-matrix-ii/description/

import numpy as np

n = 5
def løsning(n):
    matrise = np.full((n, n), np.nan)
    
    def fyll_ytre(k):
        if 2*k-1 > n:
            return
        if 2*k-1 == n:
            matrise[(n-1)//2][(n-1)//2] = n**2
            return
        
        # øvre
        for i in range(n-2*k-1):
            matrise[k][k+i] = n**2-(n-2*k)**2+i+1
        # høyre
        for i in range(n-2*k-1):
            matrise[k+i][len(matrise)-1-k] = n**2-(n-2*k)**2+i+1+(n-2*k-1)
        # nedre
        for i in range(n-2*k-1):
            matrise[len(matrise)-1-k][len(matrise)-1-k-i] = n**2-(n-2*k)**2+i+1+(n-2*k-1)*2
        # venstre
        for i in range(n-2*k-1):
            matrise[len(matrise)-1-k-i][k] = n**2-(n-2*k)**2+i+1+(n-2*k-1)*3
        fyll_ytre(k+1)

    fyll_ytre(0)
    return [[int(el) for el in e] for e in matrise]

print(løsning(n))