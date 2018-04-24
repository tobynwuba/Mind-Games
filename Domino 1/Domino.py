"""
Written to work for both Domino 1 and 2
"""
from random import sample

global target, done, length
length = 6
target = 13
done = False
arr = [[0] * length for _ in xrange(length)]
gs = file('GameState.txt', 'r')
possible_moves = set([tuple(map(int, gs.readline().split())) for _ in xrange(49)])
for moves in list(possible_moves):
    if sum(moves) > target:
        possible_moves.discard(moves)


def forward_checking(r, c):
    col = 0
    for i in xrange(length):
        col += arr[i][c]
    row1 = sum(arr[r])
    row2 = sum(arr[r+1])
    diagonal1 = calculate_diagonal1()
    diagonal2 = calculate_diagonal2()
    if r == c:
        row1 = max(row1, diagonal1)
    elif r + 1 == c:
        row2 = max(row2, diagonal2)
    elif r == length - 1 - c:
        row1 = max(row1, diagonal1)
    elif r + 1 == length - 1 - c:
        row2 = max(row2, diagonal2)
    copy_moves = possible_moves.copy()
    col, row1, row2 = target - col, target - row1, target - row2
    for i in list(possible_moves):
        if c == length - 1:
            if i[0] != row1 or i[1] != row2:
                copy_moves.discard(i)
        if r == length - 2:
            if sum(i) != col:
                copy_moves.discard(i)
        if (r, c) == (length - 2, 1):
            if i[0] != target - diagonal2:
                copy_moves.discard(i)
        if (r, c) == (length - 2, length - 1):
            if i[1] != target - diagonal1:
                copy_moves.discard(i)
        if sum(i) > col or i[0] > row1 or i[1] > row2:
            copy_moves.discard(i)
    return list(copy_moves)


def calculate_diagonal1():
    diagonal = 0
    for i in xrange(length):
        for j in xrange(length):
            if i == j:
                diagonal += arr[i][j]
    return diagonal


def calculate_diagonal2():
    diagonal = 0
    for i in xrange(length):
        for j in xrange(length):
            if i == length - 1 - j:
                diagonal += arr[i][j]
    return diagonal


def dfs(level=0):
    for s in sample(list(possible_moves), len(possible_moves)):
        arr[0][0], arr[1][0] = s
        possible_moves.remove(s)
        possible_moves.discard(s[::-1])
        dfs_visit(level + 1)
        possible_moves.add(s)
        possible_moves.add(s[::-1])
        if done:
            return


def dfs_visit(level):
    global done
    # if level > 7:
    #     return
    # elif level < 4:
    #     row, col = 0, level
    # else:
    #     row, col = 2, level - 4
    if level > 17:
        return
    elif level < 6:
        row, col = 0, level
    elif level < 12:
        row, col = 2, level - 6
    else:
        row, col = 4, level - 12
    iterate_moves = forward_checking(row, col)
    for v in sample(iterate_moves, len(iterate_moves)):
        arr[row][col], arr[row + 1][col] = v
        possible_moves.discard(v)
        possible_moves.discard(v[::-1])
        if level == 17:
            done = True
            return
        dfs_visit(level + 1)
        if done:
            return
        arr[row][col], arr[row + 1][col] = [0, 0]
        possible_moves.add(v)
        possible_moves.add(v[::-1])


dfs()
for piece in arr:
    print piece