"""
Input is the Game State of the infection Board Game, output the best move for player 2
"""

from copy import deepcopy

def play():
    depth = [3]
    game_state = open('GameState.txt', 'r')
    around = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
    chosen_move = [0]
    positions = {0: set(), 1: set(), 2: set()}
    board = game_state.readlines()
    global size
    size = len(board)
    for i in xrange(size):
        row = map(int, board[i].split())
        for j in xrange(size):
            positions[row[j]].add((i, j))
    game_state.close()

    def dfs(s,level=1, past_minimax = 0):
        idx = ((level) % 2) + 1
        minimax = (-1) ** level * float('inf')
        if level > depth[0]:
            return
        for r1, c1 in s[idx]:
            if level != 1 and level % 2:
                if minimax >= past_minimax:
                    return
            elif not level % 2:
                if minimax <= past_minimax:
                    return
            for r in xrange(-2, 3):
                for c in xrange(-2, 3):
                    if (r, c) == (0, 0):
                        continue
                    r2, c2 = [r1 + r, c1 + c]
                    arr = deepcopy(s)
                    arr = move(arr, r1, c1, r2, c2, idx)
                    if sorted(arr[idx]) == sorted(s[idx]):
                        continue
                    #else: print arr[1]
                    dfs(arr, level + 1, minimax)
                    if idx == 2:
                        minimax = maxi(arr, level, minimax, [r1, c1, r2, c2])
                    else:
                        minimax = mini(arr, minimax)

    def maxi(arr, level, minimax,  moves):
        if len(arr[2]) > minimax:
            minimax = len(arr[2])
            if level == 1:
                chosen_move[0] = moves
        return minimax

    def mini(arr, minimax):
        return min(minimax, len(arr[2]))

    def move(arr, r1, c1, r2, c2, idx):
        if (r2, c2) not in arr[0]:
            return arr
        else:
            return possible_move(arr, r1, c1, r2, c2, idx)

    def possible_move(arr, r1, c1, r2, c2, idx):
        tot = [r1, c1, r2, c2]
        global size
        diff = [abs(r2 - r1), abs(c2 - c1)]
        if min(tot) < 0 or max(tot) >= size:
            return arr
        elif max(diff) == 1:
            arr[idx].add((r2, c2))
            arr[0].remove((r2, c2))
        elif max(diff) == 2:
            arr[idx].add((r2, c2))
            arr[idx].remove((r1, c1))
        return change(arr, idx, r2, c2)

    def change(arr, idx, r2, c2):
        for i, j in around:
            r3, c3 = [r2 + i, c2 + j]
            if min(r3, c3) < 0 or max(r3, c3) > 5: continue
            other = (idx % 2) + 1
            if (r3, c3) in arr[other]:
                arr[other].remove((r3, c3))
                arr[idx].add((r3, c3))
        return arr

    #print positions
    dfs(positions)
    # change the text file
    ans = chosen_move[0]
    #print ans
    r1, c1, r2, c2 = ans
    positions = move(positions, r1, c1, r2, c2, 2)
    rewrite = open('GameState.txt', 'w')
    arr = [[0] * size for _ in xrange(size)]
    for i in xrange(1,3):
        for r, c in positions[i]:
            arr[r][c] = i
    for i in xrange(size):
        print >> rewrite, " ".join(map(str, arr[i]))
    rewrite.close()

# print timeit("play()", setup="from __main__ import play", number=2)