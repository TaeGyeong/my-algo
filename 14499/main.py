from collections import deque
N, M, x, y, K = map(int, input().split())
map_ = [list(map(int, input().split())) for _ in range(N)]
move_arr = list(map(int, input().split()))

diceX = deque([0, 0, 0, 0])
diceY = deque([0, 0, 0, 0])
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)

def rolling(d):
    if dx[d] == 1:
        temp = diceX.popleft()
        diceX.append(temp)
        diceY[0], diceY[2] = diceX[0], diceX[2]
    elif dx[d] == -1:
        temp = diceX.pop()
        diceX.appendleft(temp)
        diceY[0], diceY[2] = diceX[0], diceX[2]
    elif dy[d] == 1:
        temp = diceY.popleft()
        diceY.append(temp)
        diceX[0], diceX[2] = diceY[0], diceY[2]
    elif dy[d] == -1:
        temp = diceY.pop()
        diceY.appendleft(temp)
        diceX[0], diceX[2] = diceY[0], diceY[2]

def move(d):
    global x, y
    tx, ty = x+dx[d-1], y+dy[d-1]
    if tx<0 or ty<0 or tx>=N or ty>=M:
        return
    rolling(d-1)
    if map_[tx][ty] == 0:
        map_[tx][ty] = diceX[0]
    else:
        diceX[0] = diceY[0] = map_[tx][ty]
        map_[tx][ty] = 0
    x, y = tx, ty
    print(diceX[2])

def iter():
    for direction in move_arr:
        move(direction)
iter()