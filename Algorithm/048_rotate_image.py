# https://leetcode.com/problems/rotate-image/description/
matrix = [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
]

def løsning(matrise):
    n = len(matrise)

    def roter_ytre(k):
        if 2*k-1 >= n:
            return

        for i in range(n-2*k-1):
            (
                matrise[k+i][len(matrise)-1-k],
                matrise[len(matrise)-1-k-i][k],
                matrise[len(matrise)-1-k][len(matrise)-1-k-i], 
                matrise[k][k+i]) = (
                    matrise[k][k+i],
                    matrise[len(matrise)-1-k][len(matrise)-1-k-i],
                    matrise[k+i][len(matrise)-1-k],
                    matrise[len(matrise)-1-k-i][k]
                )
        roter_ytre(k+1)

    roter_ytre(0)
    return matrise
print(løsning(matrix))