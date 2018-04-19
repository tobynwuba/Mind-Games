from copy import deepcopy
from timeit import a
adj_list = range(-4, 5)
adj_list.remove(0)


def read_game_state():
    data = open("GameState.txt", "r")
    positions = {}
    for r in xrange(4):
        row = map(int, data.readline().split())
        for p in xrange(len(row)):
            if row[p] != 0:
                positions[row[p]] = (r, p)
    return positions


def bfs(positions):
    position_lst = tuple(positions.items())
    parent = {position_lst: None}
    frontier = [position_lst]
    while 1:
        nexti = []
        for u in frontier:
            curr_pos = dict(u)
            for piece in curr_pos:
                r1, c1 = curr_pos[piece]
                for r in adj_list:
                    r2 = r + r1
                    if r2 >= 4 or r2 < 0:
                        continue
                    for c in [r, -r]:
                        c2 = c + c1
                        if c2 >= 5 or c2 < 0:
                            continue
                        posible = check_move(curr_pos, piece, r2, c2)
                        if not posible:
                            continue
                        new_pos = deepcopy(curr_pos)
                        new_pos[piece] = (r2, c2)
                        new_pos_lst = tuple(new_pos.items())
                        if new_pos_lst not in parent:
                            parent[new_pos_lst] = u
                            nexti.append(new_pos_lst)
                            if check_goal(new_pos):
                                return [new_pos_lst, parent]
        frontier = nexti


def check_move(position, piece, r, c):
    if piece > 4:
        other_piece = range(1, 5)
    else:
        other_piece = range(5, 9)
    for i in xrange(1, 9):
        if (r, c) == position[i]:
            return False
    for opp in other_piece:
        r_other, c_other = position[opp]
        if abs(r_other - r) == abs(c_other - c):
            return False
    return True


def check_goal(position):
    for i in xrange(1, 9):
        if position[i][1] != 4 and i < 5:
            return False
        elif position[i][1] != 0 and i > 4:
            return False
    return True


position = read_game_state()
# print position
# raw_input()
ans, parent = bfs(position)

arr = []
while ans is not None:
    arr.append(ans)
    ans = parent[ans]

print 'DONE!!' + '\n'
print "No of steps = " + str(len(arr)-1)

for i in arr[::-1]:
    print i
    raw_input()