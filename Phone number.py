
import random as r
# n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def create_phone_number(n):
    num = "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
    print(num)
    return num

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])