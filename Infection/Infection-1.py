around = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]
dev = [2,1]
i, idx = [1,0]
score = [2,2]
prompt = ['Player 1: ', 'Player 2: ']

def getStartState():
    """
    Gets start state from F=GameState.txt (I don't really why I did this)
    """
    arr = []
    d = open('GameState.txt','r')
    for _ in xrange(6):
        arr.append(map(int, d.readline().split()))
    return arr

def Move(arr,r1,c1,r2,c2,idx):
    if arr[r1][c1] in [0,dev[idx]] or arr[r2][c2] != 0 :
        ans = 0
    else:        
        ans = possibleMove(r1,c1,r2,c2)
    if ans == 0: print 'bad move, try again'
    elif ans == 1: arr[r2][c2] = arr[r1][c1]
    else: arr[r2][c2], arr[r1][c1]  = arr[r1][c1], 0
    return ans

def Change(arr, idx, r2, c2, score):
    for i, j in around:
        r3, c3 = [r2 + i, c2 + j]
        if min(r3,c3) < 0: continue
        if arr[r3][c3] == dev[idx]:
            score[idx] += 1
            score[idx - 1] -= 1
            arr[r2+i][c2+j] = dev[idx - 1]
    return arr


def possibleMove(r1,c1,r2,c2):
    tot = [r1,c1,r2,c2]
    diff = [abs(r2-r1), abs(c2-c1)]
    if min(tot) < 0 or max(tot) > 6: return 0    
    elif max(diff) == 1: return 1
    elif max(diff) == 2 and min(diff) != 1: return 2
    return 0

def printArr(arr,score):
    for i in arr: print i
    a, b = score
    print "Player 1: " + str(a)
    print "Player 2: " + str(b)
    return 36 - sum(score)

arr =  getStartState()
printArr(arr, score)
while i != 0:
    r1,c1,r2,c2 = map(int, raw_input(prompt[idx]).split())
    ans = Move(arr, r1,c1,r2,c2,idx)
    if ans != 0:
        if ans == 1: score[idx] += 1
        Change(arr,idx,r2,c2,score)
        idx = (idx + 1) % 2
        i = printArr(arr,score)
z