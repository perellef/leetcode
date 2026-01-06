# https://leetcode.com/problems/generate-parentheses/

n = 3

def løsning(n):
    s = set(("()",))
    for _ in range(n-1):
        ny_s = set()
        for e in s:
            for i in range(len(e)):
                ny_s.add(e[:i]+"()"+e[i:])
        s = ny_s
    return list(s)

print(løsning(n))