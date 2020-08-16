def iq_test(numbers):
    list = numbers.split()
    odd = []
    even = []
    for i in list:
        even.append(i) if (int(i) % 2 == 0) else odd.append(i)
    if len(even) > len(odd):
        return print(list.index(odd[0]) + 1)
    else:
        return print(list.index(even[0]) + 1)

n1 = "2 4 7 8 10"
n2 = "1 2 2"
iq_test(n1)