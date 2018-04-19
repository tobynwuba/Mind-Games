from copy import deepcopy

game_state = open('GameState.txt', 'r')
positions = {0: set(), 1: set(), 2: set()}
moves = [[0, 2], [0, -2], [2, 0], [-2, 0]]
parent = {}
mem = set()
ans = []
GS = []
for i in xrange(7):
    row = map(int, game_state.readline().split())
    GS.append(row)
    for j in xrange(7):
        positions[row[j]].add((i, j))


def check_valid(r1, c1, r2, c2, r, c):
    ans, mid = False, (r/2, c/2)
    mid = (r1 + mid[0], c1 + mid[1])
    if (r1, c1) in positions[1] and (r2, c2) in positions[2] and mid in positions[1]:
        ans = True
    return [ans, mid]


def make_move(fromm, mid, to):
    positions[1].remove(fromm)
    positions[2].add(fromm)
    positions[1].remove(mid)
    positions[2].add(mid)
    positions[2].remove(to)
    positions[1].add(to)


def unmake_move(fromm, mid, to):
    positions[2].remove(fromm)
    positions[1].add(fromm)
    positions[2].remove(mid)
    positions[1].add(mid)
    positions[1].remove(to)
    positions[2].add(to)


def dfs():
    # print(GS)
    for r1, c1 in positions[1]:
        for r, c in moves:
            r2, c2 = [r1 + r, c1 + c]
            [possible, mid] = check_valid(r1, c1, r2, c2, r, c)
            if not possible:
                continue
            fromm, mid, to = [(r1, c1), mid, (r2, c2)]
            last = dfs_visit(fromm, mid, to)
            if last != 0:
                parent[to] = fromm
                return last


def dfs_visit(fromm, mid, to):
    make_move(fromm, mid, to)
    last = 0
    position = tuple(sorted(positions[1]))
    if position not in mem:
        mem.add(position)
        for r1, c1 in position:
            for r, c in moves:
                if len(positions[1]) == 1:
                    ans.append([fromm, to])
                    unmake_move(fromm, mid, to)
                    return to
                r2, c2 = [r1 + r, c1 + c]
                [valid, mid_] = check_valid(r1, c1, r2, c2, r, c)
                if not valid:
                    continue
                fromm_, mid_, to_ = [(r1, c1), mid_, (r2, c2)]
                last = dfs_visit(fromm_, mid_, to_)
                if last != 0:
                    ans.append([fromm, to])
                    unmake_move(fromm, mid, to)
                    return last
    unmake_move(fromm, mid, to)
    if last != 0:
        ans.append([fromm, to])
    return last


last = dfs()
print "done"
for i in ans[::-1]:
    print i
    raw_input("Enter for next move")



