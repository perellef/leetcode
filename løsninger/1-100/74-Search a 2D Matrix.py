# https://leetcode.com/problems/search-a-2d-matrix/description/

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

def løsning(matrix, target):
    n = len(matrix)
    m = len(matrix[0])

    nedre = 0
    øvre = n*m-1

    while øvre-nedre >= 0:
        midt = nedre + (øvre-nedre)//2

        verdi = matrix[midt//m][midt%m]
        if target < verdi:
            øvre = midt-1
        elif target > verdi:
            nedre = midt+1
        else:
            return True
        
        if øvre-nedre < 0:
            break

    return False

print(løsning(matrix, target))