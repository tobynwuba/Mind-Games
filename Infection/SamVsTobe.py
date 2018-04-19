from infection_sam import play as sam
from infection_tobe import play as tobe

arr = [10] * 3
idx = 1


while arr[0] != 0 and arr[1] != 0 and arr[2] != 0:
    if idx % 2:
        sam()
    else:
        tobe()
    idx += 1
    data = open('GameState.txt', 'r')
    arr = [0] * 3
    for i in xrange(7):
        row = map(int, data.readline().split())
        for j in row:
            arr[j] += 1
    data.close()
    print "Samuel score =" + str(arr[1])
    print "Tobe score =" + str(arr[2])
    print
print 'end!'