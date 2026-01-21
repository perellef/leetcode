# https://leetcode.com/problems/merge-intervals/description/

intervals = [[1,4],[2,3]]

def løsning(intervals):

    ints = list(sorted(intervals, key=lambda x: x[0]))

    nye = []

    i = 0
    while i < len(intervals):
        k = 0
        m = ints[i][1]
        while i+k < len(intervals):
            if m < ints[i+k][0]:
                break
            m = max(m, ints[i+k][1])
            k += 1

        nye.append([ints[i][0], m])
        i = i + k
    return nye

print(løsning(intervals))