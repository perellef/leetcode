# https://leetcode.com/problems/longest-common-prefix/

strs = ["flower","flow","flight"]

def løsning(strs):
    prefix = []
    for zipped in zip(*strs):
        if len(set(zipped)) > 1:
            break
        prefix.append(zipped[0])
    return''.join(prefix)

print(løsning(strs))
