from itertools import permutations
# def locate(i, j, value):
    
def move(w, tempBoard1):
    tempBoard2 = [[0 for _ in range(N)] for _ in range(N)]
    if w == 'U':
        for j in range(N):
            i, idx, temp = 0, 0, 0
            while i < N:
                if tempBoard1[i][j] == 0:
                    pass
                else:
                    if not temp:
                        temp = tempBoard1[i][j]
                    else:
                        if temp == tempBoard1[i][j]:
                            tempBoard2[idx][j] = 2 * temp
                            idx = idx + 1
                            temp = 0
                        else:
                            tempBoard2[idx][j] = temp
                            idx = idx + 1
                            temp = tempBoard1[i][j]
                i = i + 1
            if temp:
                tempBoard2[idx][j] = temp
    elif w == 'D':
        for j in range(N):
            i, idx ,temp = N-1, N-1, 0
            while i > -1:
                if tempBoard1[i][j] == 0:
                    i =  i - 1
                    continue
                else:
                    if not temp:
                        temp = tempBoard1[i][j]
                    else:
                        if temp == tempBoard1[i][j]:
                            tempBoard2[idx][j] = 2 * temp
                            idx = idx - 1
                            temp = 0
                        else:
                            tempBoard2[idx][j] = temp
                            idx = idx - 1
                            temp = tempBoard1[i][j]
                i = i - 1
            if temp:
                tempBoard2[idx][j] = temp

    elif w == 'R':
        for i in range(N):
            j, idx ,temp = N-1, N-1, 0
            while j > -1:
                if tempBoard1[i][j] == 0:
                    j = j - 1
                    continue
                else:
                    if not temp:
                        temp = tempBoard1[i][j]
                    else:
                        if temp == tempBoard1[i][j]:
                            tempBoard2[i][idx] = 2 * temp
                            idx = idx - 1
                            temp = 0
                        else:
                            tempBoard2[i][idx] = temp
                            idx = idx - 1
                            temp = tempBoard1[i][j]
                j = j - 1
            if temp:
                tempBoard2[i][idx] = temp
    elif w == 'L':
        for i in range(N):
            j, idx ,temp = 0, 0, 0
            while j < N:
                if tempBoard1[i][j] == 0:
                    j = j + 1
                    continue
                else:
                    if not temp:
                        temp = tempBoard1[i][j]
                    else:
                        if temp == tempBoard1[i][j]:
                            tempBoard2[i][idx] = 2 * temp
                            idx = idx + 1
                            temp = 0
                        else:
                            tempBoard2[i][idx] = temp
                            idx = idx + 1
                            temp = tempBoard1[i][j]
                j = j + 1
            if temp:
                tempBoard2[i][idx] = temp
    return tempBoard2

def moveIter(p):
    max = 0
    for i in p:
        tempBoard = board[:]
        for way in i:
            tempBoard = move(way, tempBoard)
        for x in range(N):
            for y in range(N):
                if max < tempBoard[x][y]:
                    max = tempBoard[x][y]
    return max
                    
        
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
tryCase = ['U', 'D', 'L', 'R'] # 왼 오 위 아래
maxValue = 0
for i in range(4):
    a = tryCase[:]
    a.append(tryCase[i])
    perm = permutations(a)
    val = moveIter(perm)
    if maxValue < val:
        maxValue = val
print(maxValue)