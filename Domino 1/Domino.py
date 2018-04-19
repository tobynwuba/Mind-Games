"""
Written to work for both Domino 1 and 2
"""


length = 4
arr = [[0] * length for _ in xrange(length)]
gs = file('GameState.txt', 'r')
global target, done
target = 6
done = False
possible_moves = set([tuple(map(int, gs.readline().split())) for _ in xrange(28)])


def check():
    row = [0] * len(arr)
    diag1 = 0
    diag2 = 0
    global target
    for i in xrange(len(arr)):
        if sum(arr[i]) > target:
            return False
        for j in xrange(len(arr)):
            row[j] += arr[i][j]
            if i == j:
                diag1 += arr[i][j]
            if i == len(arr) - 1 - j:
                diag2 += arr[i][j]
            if row[j] > target or diag1 > target or diag2 > target:
                return False
    return True


def check_final():
    row = [0] * len(arr)
    diag1 = 0
    diag2 = 0
    global target
    for i in xrange(len(arr)):
        if sum(arr[i]) != target:
            return False
        for j in xrange(len(arr)):
            row[j] += arr[i][j]
            if i == j:
                diag1 += arr[i][j]
            if i == len(arr) - 1 - j:
                diag2 += arr[i][j]
    for j in xrange(len(arr)):
        if row[j] != target or diag1 != target or diag2 != target:
            return False
    return True


def dfs(level=0):
    global done
    for s in list(possible_moves):
        arr[level][0], arr[level + 1][0] = s
        possible_moves.remove(s)
        possible_moves.discard(s[::-1])
        dfs_visit(level + 1)
        possible_moves.add(s)
        possible_moves.add(s[::-1])
        if done:
            return


def dfs_visit(level):
    global done
    if level > 7:
        return
    elif level < 4:
        row, col = 0, level
    else:
        row, col = 2, level - 4
    # if level > 17:
    #     return
    # elif level < 6:
    #     row, col = 0, level
    # elif level < 12:
    #     row, col = 2, level - 6
    # else:
    #     row, col = 4, level - 12
    for v in list(possible_moves):
        arr[row][col], arr[row + 1][col] = v
        possible_moves.discard(v)
        possible_moves.discard(v[::-1])
        correct = check()
        if level == 7:
            correct = check_final()
            if correct:
                done = True
                return
        if correct:
            dfs_visit(level + 1)
            if done:
                return
        arr[row][col], arr[row + 1][col] = [0, 0]
        possible_moves.add(v)
        possible_moves.add(v[::-1])


dfs()
print arr
