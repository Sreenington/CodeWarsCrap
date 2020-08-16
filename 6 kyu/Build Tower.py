def tower_builder(n_floors):
    tower = []
    for floor in range(n_floors):
        elem = ' '*((n_floors-1)-floor) + ('*'*((2*floor) + 1)) + ' '*((n_floors-1)-floor)
        tower.append(elem)
    return print(tower)
tower_builder(4)
