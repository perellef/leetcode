# https://leetcode.com/problems/zigzag-conversion/

s = "A"
num_rows = 1

def løsning():
    if num_rows == 1:
        return s

    ny_s = []
    ny_s.append(s[::(num_rows-2)*2+2])

    for i in range(1,num_rows-1):
        for k in range(i,len(s),(num_rows-2)*2+2):
            ny_s.append(s[k])

            ekstra = (num_rows-i-1)*2
            if k+ekstra < len(s):
                ny_s.append(s[k+ekstra])

    ny_s.append(s[num_rows-1::(num_rows-2)*2+2])

    return ''.join(ny_s)

print(løsning(s, num_rows))
