arr = [[0] * 6 for _ in xrange(6)]
gs = file('GameState.txt', 'r')
target = [13]
done = [False]
possible_moves = set([tuple(map(int, gs.readline().split())) for _ in xrange(28)])


def check():
    row = [0] * len(arr)
    diag1 = 0
    diag2 = 0
    for i in xrange(len(arr)):
        if sum(arr[i]) > target[0]:
            return False
        for j in xrange(len(arr)):
            row[j] += arr[i][j]
            if i == j:
                diag1 += arr[i][j]
            if i == len(arr) - 1 - j:
                diag2 += arr[i][j]
            if row[j] > target[0] or diag1 > target[0] or diag2 > target[0]:
                return False
    return True


def check_final():
    row = [0] * len(arr)
    diag1 = 0
    diag2 = 0
    for i in xrange(len(arr)):
        if sum(arr[i]) != target[0]:
            return False
        for j in xrange(len(arr)):
            row[j] += arr[i][j]
            if i == j:
                diag1 += arr[i][j]
            if i == len(arr) - 1 - j:
                diag2 += arr[i][j]
    for j in xrange(len(arr)):
        if row[j] != target[0] or diag1 != target[0] or diag2 != target[0]:
            return False
    return True


def dfs(level=0):
    for s in list(possible_moves):
        arr[level][0], arr[level + 1][0] = s
        possible_moves.remove(s)
        possible_moves.discard(s[::-1])
        dfs_visit(level + 1)
        possible_moves.add(s)
        possible_moves.add(s[::-1])
        if done[0]:
            return


def dfs_visit(level):
    if level > 17:
        return
    elif level < 6:
        row, col = 0, level
    elif level < 12:
        row, col = 2, level - 6
    else:
        row, col = 4, level - 12
    for v in list(possible_moves):
        arr[row][col], arr[row + 1][col] = v
        possible_moves.discard(v)
        possible_moves.discard(v[::-1])
        correct = check()
        if level == 17:
            correct = check_final()
            if correct:
                done[0] = True
                return
        if correct:
            dfs_visit(level + 1)
            if done[0]:
                return
        arr[row][col], arr[row + 1][col] = [0, 0]
        possible_moves.add(v)
        possible_moves.add(v[::-1])


dfs()
print arr
