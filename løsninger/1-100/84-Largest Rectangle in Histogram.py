# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

height = [2,4]

def løsning(ns):
    ns.append(0)
    
    m = 0
    reks = [[0,0]]

    i = 0
    while i < len(ns):
        antall, rek_n = reks[-1]

        if ns[i] < rek_n:
            reks.pop()
            m = max(m, antall*rek_n)
            if ns[i] > reks[-1][1]:
                reks.append([0,ns[i]])
            reks[-1][0] += antall
            continue
        elif ns[i] > rek_n:
            reks.append([1,ns[i]])
        else:
            reks[-1][0] += 1

        i += 1
    return m

print(løsning(height))