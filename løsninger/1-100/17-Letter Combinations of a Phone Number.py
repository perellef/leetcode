# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

digits = "23"

def løsning(digits):

    mulige_bokstaver = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def _rekursiv_løkke_(ds, lst):
        if ds == "":
            return lst
        
        ny_lst = []
        for e in lst:
            for tegn in mulige_bokstaver[ds[0]]:
                ny_lst.append(e+tegn)

        return _rekursiv_løkke_(ds[1:], ny_lst)
    
    return _rekursiv_løkke_(digits, [""])


print(løsning(digits))