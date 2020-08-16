import random as r

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def create_phone_number(n):
    num = ''.join(str(i) for i in n)
    num = num[:0] + '(' + num[:3] + ') ' + num[3:6] + '-' + num[6:]
    print(num)
    return num


'''
Clever Solution(Not mine)
'''


def create_phone_number(n):
    num = "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
    print(num)
    return num


create_phone_number(n)
