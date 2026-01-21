# https://leetcode.com/problems/minimum-window-substring/

s = "a"
t = "b"

from collections import defaultdict

def løsning(s,t):
    thash = defaultdict(int)
    for char in t:
        thash[char] += 1

    kun_t = [(tegn, i) for i, tegn in enumerate(s) if tegn in thash]

    if len(kun_t) == 0:
        return ""

    intervall = (0,0)
    
    start_i = 0
    slutt_i = 0

    indeks = lambda i: kun_t[i][1]
    tegn = lambda i: kun_t[i][0]

    vindu = defaultdict(int)
    vindu[tegn(start_i)] = 1
    antall = 1

    while True:
        if any((
            indeks(slutt_i)-indeks(start_i)+1 >= intervall[1]-intervall[0] and intervall[1] != 0,
            antall == len(t)
        )):
            if indeks(slutt_i)-indeks(start_i)+1 < intervall[1]-intervall[0] or intervall[1] == 0:
                intervall = (indeks(start_i), indeks(slutt_i)+1)
                
            # flytter startpeker en frem
            vindu[tegn(start_i)] -= 1
            if vindu[tegn(start_i)] < thash[tegn(start_i)]:
                antall -= 1
            start_i += 1
            if start_i == len(kun_t):
                break
            continue
        
        # flytter sluttpeker en frem
        slutt_i += 1
        if slutt_i == len(kun_t):
            break
        vindu[tegn(slutt_i)] += 1
        if vindu[tegn(slutt_i)] <= thash[tegn(slutt_i)]:
            antall += 1

    return s[intervall[0]:intervall[1]]
    
print(løsning(s, t))