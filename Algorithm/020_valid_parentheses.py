# https://leetcode.com/problems/valid-parentheses/

s = "([])"

def løsning(s):
    if len(s) % 2 == 1:
        return False

    while True:
        før = len(s)
        s = s.replace(r"{}", "").replace("[]", "").replace("()", "")
        
        if len(s) == før:
            return False
        if len(s) == 0:
            return True

print(løsning(s))