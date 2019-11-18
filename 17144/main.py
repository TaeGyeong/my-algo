import copy
def init(r, c, a):
    b = copy.deepcopy(a)
    for i in range(r):
        for j in range(c):
            if int(b[i][j]) != -1:
                b[i][j] = 0
            else:
                b[i][j] = -1
    return b

def makeResult(a, i, j, r, c, result):
    if int(a[i][j]) == 0:
        pass
    elif int(a[i][j]) == -1:
        pass
    else:
        dx, dy = (-1, 0, 1, 0), (0, -1, 0, 1)
        spreadCount = 0
        spread = int(int(a[i][j]) / 5)
        for idx in range(4):
            if i+dx[idx] < 0 or i+dx[idx] == r or j+dy[idx] < 0 or j+dy[idx] == c:
                pass
            elif result[i+dx[idx]][j+dy[idx]] == -1:
                pass
            else:
                result[i+dx[idx]][j+dy[idx]] += spread
                spreadCount += 1
        
        rest = int(a[i][j]) - spread * spreadCount 
        result[i][j] += rest

def airClean(result, r, c):
    cleaner = []
    for i in range(r):
        if int(result[i][0]) == -1:
            cleaner.append(i)
            cleaner.append(i+1)
            break
    moveVal = 0
    for i in range(1, c):
        temp = result[cleaner[0]][i]
        result[cleaner[0]][i] = moveVal
        moveVal = temp
    for i in range(cleaner[0]-1, -1, -1):
        temp = result[i][c-1]
        result[i][c-1] = moveVal
        moveVal = temp
    for i in range(c-2, -1, -1):
        temp = result[0][i]
        result[0][i] = moveVal
        moveVal = temp
    for i in range(1, cleaner[0]):
        temp = result[i][0]
        result[i][0] = moveVal
        moveVal = temp

    moveVal = 0
    for i in range(1, c):
        temp = result[cleaner[1]][i]
        result[cleaner[1]][i] = moveVal
        moveVal = temp
    for i in range(cleaner[1]+1, r):
        temp = result[i][c-1]
        result[i][c-1] = moveVal
        moveVal = temp
    for i in range(c-2, -1, -1):
        temp = result[r-1][i]
        result[r-1][i] = moveVal
        moveVal = temp
    for i in range(r-2, cleaner[1], -1):
        temp = result[i][0]
        result[i][0] = moveVal
        moveVal = temp
    

            
def calculate(result, r, c):
    allCal = 0
    for i in range(r):
        for j in range(c):
            allCal += result[i][j]
    print(allCal+2)
    

r, c, T = map(int, input().split())
a = [list(input().split(' ')) for _ in range(r)]
result = init(r, c, a)

for cur in range(T):
    for i in range(r):
        for j in range(c):
            makeResult(a, i, j, r, c, result)

    airClean(result, r, c)
    if cur == T-1:
        break
    else:
        a = copy.deepcopy(result)
        result = init(r, c, a)

calculate(result, r, c)