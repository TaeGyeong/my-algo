dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)
def checkStack():
    for i in range(N):
        for j in range(N):
            if len(stack[i][j]) == K:
                return True
            return False

def move(idx):
    print("move idx:", idx)
    global horse
    x, y, d = horse[idx-1]
    print("x, y, d:", x, y, d)
    tx, ty = x + dx[d], y + dy[d]
    pos = stack[x][y].index(idx) # horse stack index 
    if color_map[tx][ty] == 0: # white case
        for _ in range(len(stack[x][y]) - pos):
            temp = stack[x][y].pop(pos)
            stack[tx][ty].append(temp)
            horse[idx-1][0], horse[idx-1][1] = tx, ty 
    elif color_map[tx][ty] == 1: # red case
        for _ in range(len(stack[x][y]) - pos):
            temp = stack[x][y].pop()
            stack[tx][ty].append(temp)
            horse[idx-1][0], horse[idx-1][1] = tx, ty 
    elif color_map[tx][ty] == 2: # blue case
        tx2, ty2 = x - dx[d], y - dy[d]
        if d == 0 or d == 2:
            d += 1
        else:
            d -= 1
        horse[idx][2] = d
        # 반대방향도 파란색칸인 경우
        if color_map[tx2][ty2] == 2:
            pass
        else:
            move(idx)      
        

def playRound():
    turn = 0
    while True:
        for i in range(1, K+1):
            move(i)
        turn += 1
        if checkStack():
            break
    return turn

N, K = map(int, input().split())
color_map = list()
for _ in range(N):
    color_map.append(list(map(int, input().split())))

stack = [[[] for _ in range(N)] for _ in range(N)]
horse = list()
for i in range(1, K+1):
    tx, ty, direction = map(int, input().split())
    stack[tx-1][ty-1].append(i)
    horse.append([tx-1, ty-1, direction-1]) # direction: 1부터 순서대로 →, ←, ↑, ↓의 의미

print(playRound())