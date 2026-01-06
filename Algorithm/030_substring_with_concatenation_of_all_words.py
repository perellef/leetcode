# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

s = "abca"
words = ["a","b","c"]

from collections import defaultdict

def løsning(s, words):

    if len(set(words)) == 1:
        words = [''.join(words)]

    wordlen = len(words[0])
    if len(words) == 1:
        return [i for i in range(len(s)) if s[i:i+wordlen] == words[0]]

    wordnum = defaultdict(int)
    for word in words:
        wordnum[word] += 1

    indekser = []
    concats = {}
    for i in range(len(s)):
        substr = s[i:i+len(words[0])]
        if substr in wordnum:
            for k,(antall,h) in list(concats.items()):
                if (k-i) % wordlen != 0:
                    continue
                if h[substr] == wordnum[substr]:
                    del concats[k]
                    continue

                if antall+1 == len(words):
                    indekser.append(k)
                    del concats[k]
                    continue

                concats[k] = (concats[k][0]+1, concats[k][1])
                concats[k][1][substr] += 1

            if len(s)-i > len(words):
                concats[i] = (1, defaultdict(int))
                concats[i][1][substr] = 1
        else:
            concats = {k:v for k,v in concats.items() if (k-i) % wordlen != 0}  

    return indekser      

print(løsning(s, words))