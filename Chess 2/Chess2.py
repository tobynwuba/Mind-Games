"""
This code is meant to solve the Chess stages for microsoft mind games, takes the game state as input and outputs the
moves sequencially
"""
from copy import deepcopy
# from timeit import timeit

adj_list = range(-4, 5)
adj_list.remove(0)
memo = set()


def read_game_state():
    data = open("GameState.txt", "r")
    string = ""
    for r in xrange(4):
        row = data.readline().split()
        string += ''.join(row)
    return int(string)


def int_to_dict(number):
    string = str(number)
    positions = {}
    for r in xrange(4):
        strt = 5 * r
        row = string[strt : strt + 5]
        for p in xrange(len(row)):
            if int(row[p]) != 0:
                positions[int(row[p])] = (r, p)
    return positions

def hash_it(pos):
    arr = [[0] * 5 for _ in xrange(4)]
    for i in pos:
        r, c = pos[i]
        arr[r][c] = i
    string = ''.join([''.join(map(str, arr[i])) for i in xrange(4)])
    string_lst = map(int, list(string))
    if len(string) < 20:
        print 'a'
    for i in xrange(len(string_lst)):
        if 0 < string_lst[i] <= 4:
            string_lst[i] = 1
        elif string_lst[i] > 4 :
            string_lst[i] = 2
    string2 = ''.join(map(str, string_lst))
    return [string2, string]

def bfs(positions):
    mem_value, position_lst = hash_it(positions)
    memo.add(mem_value)
    parent = {position_lst: None}
    frontier = [position_lst]
    while 1:
        nexti = []
        for u in frontier:
            curr_pos = int_to_dict(u)
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
                        mem_value, new_pos_lst = hash_it(new_pos)
                        if mem_value not in memo:
                            parent[new_pos_lst] = u
                            memo.add(mem_value)
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


number = read_game_state()
position = int_to_dict(number)
# print position
# raw_input()
ans, parent = bfs(position)

arr = []
while ans is not None:
    arr.append(ans)
    ans = parent[ans]

print 'DONE!!'
print "No of steps = " + str(len(arr)-1)


for i in arr[::-1]:
    for j in xrange(4):
        i = str(i)
        strt = 5 * j
        print i[strt: strt + 5]
    raw_input()