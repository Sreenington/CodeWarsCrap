def move_zeros(array):
    ans = []
    for i in array:
        if i !=0 or i is False:
            ans.append(i)
    for i in array:
        if i == 0 and i is not False and len(array) >= 1:
            ans.append(i)
    return print(ans)

def move_zeroz(array):
    return print(sorted(array, key=lambda x: x == 0 and x is not False))


a1 = [1,2,0,1,0,1,0,3,0,1]
a2 = ["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]
a3 = [0, False, 0, 'c', 0, False, 'z', 2, -6, 'b', 3, 9, 'y', -8, False, 3, '0', -9, -7, False, 0, 0, False, 0, 'y', 0, False, 6, False, 0, -2, 0, -2, 'x', True]
move_zeroz(a2)