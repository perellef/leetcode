# https://leetcode.com/problems/median-of-two-sorted-arrays/

nums1 = [1,2,3]
nums2 = [1,1,2]

def median(ns):
    if len(ns) % 2 == 0:
        return (ns[len(ns)//2-1]+ns[len(ns)//2])/2
    return ns[(len(ns)-1)//2]

def reduser(ns1,ns2):
    if min(len(ns1), len(ns2)) <= 3:
        return ns1, ns2
    
    m1 = median(ns1)
    m2 = median(ns2)

    fjernes = min(
        (len(ns1)-1)//2,
        (len(ns2)-1)//2,
        len(ns1)-3,
        len(ns2)-3,
    )

    if m1 < m2:
        ny_ns1 = ns1[fjernes:] 
        ny_ns2 = ns2[:len(ns2)-fjernes] 
        return reduser(ny_ns1, ny_ns2)
    else:
        ny_ns2 = ns2[fjernes:] 
        ny_ns1 = ns1[:len(ns1)-fjernes] 
        return reduser(ny_ns1, ny_ns2)

def løsning():

    ns1, ns2 = reduser(nums1, nums2)

    if len(ns1) > len(ns2):
        ns1,ns2 = ns2,ns1

    for n1 in ns1:
        if n1 >= ns2[-1]:
            ns2.append(n1)
            continue

        for i,n2 in enumerate(ns2):
            if n1 <= n2:
                ns2.insert(i, n1)
                break

    if len(ns2) % 2 == 1:
        median = ns2[(len(ns2)-1)//2]
    else:
        median = (ns2[(len(ns2))//2-1]+ns2[(len(ns2))//2])/2
    return median

print(løsning(nums1, nums2))