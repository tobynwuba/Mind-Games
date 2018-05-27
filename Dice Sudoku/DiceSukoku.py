from random import sample

global length, done

length = 9
done = False
arr_row, arr_col, arr_box = [[set() for _ in xrange(length)] for _ in xrange(3)]
arr = []
blanks = []
ans = {}

gs = file('GameState.txt', 'r')

for row in xrange(length):
    line_arr = map(int, gs.readline().split())
    arr.append(line_arr)
    for col in xrange(length):
        num = line_arr[col]
        if num != 0:
            arr_row[row].add(num)
            arr_col[col].add(num)
            box_pos = ((row / 3) * 3) + (col / 3)
            arr_box[box_pos].add(num)
        else:
            blanks.append((row,col))
# print arr_row
# print arr_col
# print arr_box


def remove(r, c, box, number):
    arr_row[r].discard(number)
    arr_col[c].discard(number)
    arr_box[box].discard(number)


def replace(r, c, box, number):
    arr_row[r].add(number)
    arr_col[c].add(number)
    arr_box[box].add(number)


def dfs(level=0):
    r, c = blanks[level]
    box = (r / 3) * 3 + (c / 3)
    union = arr_row[r].union(arr_col[c]).union(arr_box[box])
    remaining = set(range(1, length + 1)).difference(union)
    for numb in list(remaining):
        replace(r, c, box, numb)
        ans[(r, c)] = numb
        dfs_visit(level + 1)
        if done:
            return
        remove(r, c, box, numb)
        del ans[(r, c)]


def dfs_visit(level):
    global done
    if level == len(blanks):
        done = True
        return
    r, c = blanks[level]
    box = (r / 3) * 3 + (c / 3)
    union = arr_row[r].union(arr_col[c]).union(arr_box[box])
    remaining = set(range(1, length + 1)).difference(union)
    for numb in list(remaining):
        replace(r, c, box, numb)
        ans[(r, c)] = numb
        dfs_visit(level + 1)
        if done:
            return
        remove(r, c, box, numb)
        del ans[(r, c)]


dfs()
array = [[0] * length for _ in xrange(length)]
for (r, c), value in ans.items():
    array[r][c] = value
print array