dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)
def checkStack():
    for x, y, d in horse:
        if len(stack[x][y]) >= 4:
            return True
    return False

def move(idx):
    # print("move idx:", idx)
    global horse, stack
    x, y, d = horse[idx-1]
    # print("x, y, d:", x, y, d)
    tx, ty = x + dx[d], y + dy[d]
    # 이동하는 칸이 벗어나는 경우 (파란색)
    if tx < 0 or ty < 0 or tx > N-1 or ty > N-1:
        if d == 0 or d == 2:
            d += 1
        else:
            d -= 1
        tx2, ty2 = x + dx[d], y + dy[d]
        horse[idx-1][2] = d
        # 반대방향도 파란색칸인 경우
        if color_map[tx2][ty2] == 2:
            pass
        else:
            move(idx)      
    elif color_map[tx][ty] == 0: # white case
        pos = stack[x][y].index(idx) # horse stack index 
        for _ in range(len(stack[x][y]) - pos):
            temp = stack[x][y].pop(pos)
            stack[tx][ty].append(temp)
            horse[temp-1][0], horse[temp-1][1] = tx, ty 
    elif color_map[tx][ty] == 1: # red case
        pos = stack[x][y].index(idx) # horse stack index 
        for _ in range(len(stack[x][y]) - pos):
            temp = stack[x][y].pop()
            stack[tx][ty].append(temp)
            horse[temp-1][0], horse[temp-1][1] = tx, ty 
    elif color_map[tx][ty] == 2: # blue case
        if d == 0 or d == 2:
            d += 1
        else:
            d -= 1
        tx2, ty2 = x + dx[d], y + dy[d]
        horse[idx-1][2] = d
        if tx2 < 0 or ty2 < 0 or tx2 > N-1 or ty2 > N-1:
            pass
        elif color_map[tx2][ty2] == 2:
            pass
        else:
            move(idx)      
    
        

def playRound():
    turn = 0
    flag = False
    while True:
        for i in range(1, K+1):
            move(i)
            if checkStack():
                flag = True
                break
        turn += 1
        if flag:
            break
        if turn >= 1000:
            return -1
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
