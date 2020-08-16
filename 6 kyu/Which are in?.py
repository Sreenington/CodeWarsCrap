def in_array(array1, array2):
    array1 = sorted(array1)
    print(array1)
    r = []
    for i in array1:
        for j in array2:
            if j.find(i) != -1 and i not in r:
                r.append(i)
    return print(r)

a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
in_array(a1, a2)