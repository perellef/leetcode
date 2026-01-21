# https://leetcode.com/problems/trapping-rain-water/

height = [4,2,3]

def løsning(ns):
    ns_v = [(0, ns[0])]
    ns_h = [(len(ns)-1, ns[-1])]
    for i in range(1,len(ns)):
        if ns[i] > ns_v[-1][1]:
            ns_v.append((i,ns[i]))
        if ns[len(ns)-i-1] > ns_h[-1][1]:
            ns_h.append((len(ns)-i-1, ns[len(ns)-i-1]))

    f = 0
    totalarea = 0

    pv = 0
    ph = 0
    while True:
        x1,y1 = ns_v[pv]
        x2,y2 = ns_h[ph]

        totalarea += min(y1-f,y2-f)*(x2-x1+1)
        f = min(y1,y2)

        if y1 > y2:
            ph += 1
        elif y1 < y2:
            pv += 1
        if y1 == y2:
            pv += 1
            ph += 1
        
        if pv >= len(ns_v) or ph >= len(ns_h):
            break
    
    return totalarea-sum(ns)

print(løsning(height))