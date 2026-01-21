# https://leetcode.com/problems/edit-distance/

word1 = "horse"
word2 = "ros"

import math
import numpy as np

def løsning(w1,w2):
    n = len(w1)
    m = len(w2)

    D = np.full((n+1,m+1), np.nan)

    def avstand_rek(i,j):
        
        if not math.isnan(D[i,j]):
            return D[i,j]
    
        if i==0 or j==0:
            D[i,j] = max(i,j)
        elif w1[i-1]==w2[j-1]:
            D[i,j] = avstand_rek(i-1,j-1)
        else:
            D[i,j] = min(
                avstand_rek(i-1,j-1)+1,
                avstand_rek(i,j-1)+1,
                avstand_rek(i-1,j)+1,
            )

        return D[i,j]

    return int(avstand_rek(n,m))

print(løsning(word1, word2))