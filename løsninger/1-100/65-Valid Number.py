# https://leetcode.com/problems/valid-number/description/

s = "3."

desimaler = set(("0","1","2","3","4","5","6","7","8","9"))

def er_heltall(s):
    if len(s)==0:
        return False
    for tegn in s:
        if tegn not in desimaler:
            return False
    return True

def er_flyttall(s):
    if s == ".":
        return False
    if len(s)==0:
        return False
    
    punktum = False
    for tegn in s:
        if tegn == ".":
            if punktum:
                return False
            punktum = True
        elif tegn not in desimaler:
            return False
    return True


def løsning(s):
    ny_s = s.lstrip("+").lstrip("-").replace("E","e")
    if len(ny_s) < len(s)-1:
        return False
    print(ny_s)
    if "e" in ny_s:
        split = ny_s.split("e")
        if len(split) > 2:
            return False
        foran, bak = split
        bak_ny = bak.lstrip("+").lstrip("-")
        if len(bak_ny) < len(bak)-1:
            return False

        return er_flyttall(foran) and er_heltall(bak_ny) 

    return er_flyttall(s)
print(løsning(s))