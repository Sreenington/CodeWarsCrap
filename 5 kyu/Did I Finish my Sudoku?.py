def done_or_not(board):  # board[i][j]
    # print((board[1]).count())
    for i in range(0, 9):
        count = []
        for j in range(0, 9):
            count.append(board[j][i])
            continue
        if sum(count) != 45:
            return 'Try again!'
    return 'Finished!'


b1 = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
    , [4, 9, 8, 2, 6, 1, 3, 7, 5]
    , [7, 5, 6, 3, 8, 4, 2, 1, 9]

    , [6, 4, 3, 1, 5, 8, 7, 9, 2]
    , [5, 2, 1, 7, 9, 3, 8, 4, 6]
    , [9, 8, 7, 4, 2, 6, 5, 3, 1]

    , [2, 1, 4, 9, 3, 5, 6, 8, 7]
    , [3, 6, 5, 8, 1, 7, 9, 2, 4]
    , [8, 7, 9, 6, 4, 2, 1, 5, 3]]  # 'Finished!'

b2 = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
    , [4, 9, 8, 2, 6, 1, 3, 7, 5]
    , [7, 5, 6, 3, 8, 4, 2, 1, 9]

    , [6, 4, 3, 1, 5, 8, 7, 9, 2]
    , [5, 2, 1, 7, 9, 3, 8, 4, 6]
    , [9, 8, 7, 4, 2, 6, 5, 3, 1]

    , [2, 1, 4, 9, 3, 5, 6, 8, 7]
    , [3, 6, 5, 8, 1, 7, 9, 2, 4]
    , [8, 7, 9, 6, 4, 2, 1, 3, 5]]  # 'Try again!'

b3 = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
      [2, 3, 4, 5, 6, 7, 8, 9, 1],
      [3, 4, 5, 6, 7, 8, 9, 1, 2],

      [4, 5, 6, 7, 8, 9, 1, 2, 3],
      [5, 6, 7, 8, 9, 1, 2, 3, 4],
      [6, 7, 8, 9, 1, 2, 3, 4, 5],

      [7, 8, 9, 1, 2, 3, 4, 5, 6],
      [8, 9, 1, 2, 3, 4, 5, 6, 7],
      [9, 1, 2, 3, 4, 5, 6, 7, 8]]  # 'Try again!'
print(done_or_not(b3))

'''
Previous attempt 

def done_or_not(board): 
    for i in range(0,9):
        count = []
        for j in range(0,9):
            count.append(board[j][i])
            continue
        if sum(count) != 45:
            return 'Try again!'
    print(board)
    return 'Finished!'
'''
