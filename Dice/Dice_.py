global length, done
length, done = 6, False
arr = []
gs = file('GameState.txt', 'r')
[arr.append(map(int, gs.readline().split())) for _ in xrange(length)]
moves = {}
moves_made = set()
done = set()


def dfs():
    r1, c1 = [5, 0]
    done.add((r1, c1))
    number = arr[r1][c1]
    for r in xrange(-1, 1):
        for c in xrange(2):
            moves[number] = (r, c)
            moves_made.add((r,c))
            r2, c2 = [r1 + r, c1 + c]
            dfs_visit(r2, c2)
        if done:
            return


def dfs_visit(r1, c1):
    global done
    done.add((r1, c1))
    number = arr[r1][c1]
    if number == 0:
        done = True
    elif number in moves:
        r, c = moves[number]
        r2, c2 = [r1 + r, c1 + c]
        if min(r2, c2) >= 0 and max(r2, c2) < length and (r2, c2) not in done:
            dfs_visit(r2, c2)
        else:
            return number
    else:
        for r in xrange(-1, 2):
            for c in xrange(-1, 2):
                r2, c2 = [r1 + r, c1 + c]
                if min(r2, c2) >= 0 and max(r2, c2) < length and arr[r2][c2] != 0 and (r2, c2) not in done and (
                        r, c) not in moves_made:
                    moves[number] = (r, c)
                    moves_made.add((r, c))
                    bad = dfs_visit(r2, c2)
                    moves_made.discard((r, c))
                    if number != bad:
                        del moves[number]
                        return bad
    if done:
        return
    del moves[number]



dfs()
print(moves)