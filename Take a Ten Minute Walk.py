from collections import Counter

def is_valid_walk(walk):
    dir_count = (Counter(walk))
    dir_val_x = {'n': 1, 's': -1}
    dir_val_y = {'e': 1, 'w': -1}
    dx = 0
    dy = 0
    for i in dir_count:
        if i in dir_val_x:
            dx += dir_val_x[i] * dir_count[i]
        if i in dir_val_y:
            dy += dir_val_y[i] * dir_count[i]
    if len(walk) != 10 or dx != 0 or dy != 0:
        return print(False)
    else:
        return print(True)


# Test Cases
d1 = ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']  # True  passes
d2 = ['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']  # False passes
d3 = ['w']  # False passes
d4 = ['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']  # False passes
d5 = ['e', 'w', 'n', 'w', 'n', 's', 'n', 's', 'e', 'w']  # False passes
is_valid_walk(d1)
