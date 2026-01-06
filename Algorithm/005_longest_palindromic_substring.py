# https://leetcode.com/problems/longest-palindromic-substring/

s = "abab"

def er_palindrom(start, slutt):
    for i in range(slutt-start+1):
        if s[start+i] != s[slutt-i]:
            return False
    return True
    
def løsning():
    lengste = 0
    palindrome = ""
    for start in range(len(s)):
        for slutt in range(start,len(s)):
            if slutt-start + 1 > lengste and er_palindrom(start, slutt):
                lengste = slutt-start
                palindrome = s[start:slutt+1]
    return palindrome

print(løsning(s))