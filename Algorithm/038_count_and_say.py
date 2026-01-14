# https://leetcode.com/problems/count-and-say/description/

n = 4

def løsning(n):

    def RLE(s,m):
        if m == n:
            return s
        
        ny_s = []
        ant = 1
        for i in range(len(s)):
            if i == len(s)-1 or s[i] != s[i+1]:
                ny_s.append(str(ant))
                ny_s.append(s[i])
                ant = 1
                continue
            ant += 1

        return RLE(''.join(ny_s), m+1)
    return RLE("1", 1)

print(løsning(n))