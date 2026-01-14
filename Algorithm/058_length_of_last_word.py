# https://leetcode.com/problems/length-of-last-word/description/

s = "Hello World"

def løsning(s):
    siste_ord = False
    l = 0
    for tegn in reversed(s):
        if tegn == " ":
            if siste_ord:
                break
            continue
        else:
            siste_ord = True
            l += 1
    return l
print(løsning(s))