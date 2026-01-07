# https://leetcode.com/problems/maximal-rectangle/description/

matrix = [
    ["0","0","0","0","0"],
    ["1","0","0","0","0"],
    ["0","0","0","0","0"],
    ["0","0","0","0","0"]
]

from functools import reduce

def bit_and(numbers):
    return reduce(lambda x, y: x & y, numbers)

def løsning(matrix):
    binære = [int(''.join(e), 2) for e in matrix]
    flip_binære = [int(''.join(e), 2) for e in zip(*matrix)]

    maxareal = 0
    for bin_lst in (binære, flip_binære):
        for fra in range(len(bin_lst)):
            for til in range(fra, len(bin_lst)):
                bins = str(bin(bit_and(bin_lst[fra:til+1])))
                
                m = 0
                s = 0
                for t in bins:
                    if t == "1":
                        s += 1
                        m = max(m,s)
                    else:
                        s = 0
                maxareal = max(maxareal, m*(til-fra+1))

    return maxareal

print(løsning(matrix))