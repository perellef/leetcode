# https://leetcode.com/problems/spiral-matrix/description/

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

def løsning(matrise):
    m,n = len(matrise), len(matrise[0])


    lst = []
    def traverser_ytre(k):
        if min(m,n) == 2*k:
            return
        if min(m,n) == 2*k+1:
            if m > n:
                for i in range(m-2*(k)):
                    lst.append(matrise[k+i][k])
                return
            else:
                for i in range(n-2*(k)):
                    lst.append(matrise[k][k+i])
                return

        # øvre
        for i in range(n-2*k-1):
            lst.append(matrise[k][k+i])
        # høyre
        for i in range(m-2*k-1):
            lst.append(matrise[k+i][n-1-k])
        # nedre
        for i in range(n-2*k-1):
            lst.append(matrise[m-1-k][n-1-k-i])
        # venstre
        for i in range(m-2*k-1):
            lst.append(matrise[m-1-k-i][k])
    
        traverser_ytre(k+1)

    traverser_ytre(0)

    return lst

print(løsning(matrix))