def addLine(l): # 받은 라인을 순서대로 받아서 따로저장. 
    return

def solve(x, y, d, g):
    l = [(x, y)]
    if d == 0: # x좌표증가.
        l.append((x+1, y))
    elif d == 1: # y좌표감소
        l.append((x, y-1))
    elif d == 2: # x좌표 감소
        l.append((x-1, y)) 
    elif d == 3: # y좌표증가
        l.append((x, y+1))
    if g == 0:
        addLine(l)
        return
    # draw dragon curve
    for idx in range(1, g+1):
        lastIdx = len(l)
        tx, ty = l[lastIdx-1] # 끝점기준
        for k in range(lastIdx-2, -1, -1):
            targetX, targetY = l[k] # 시계방향 90도 이동하는 X, Y
            if tx == targetX:
                targetX = tx - targetX
                l.append((targetX, ty))
            elif ty == targetY:
                targetY = ty - targetY
                l.append((tx, targetY))
                
N = int(input())
temp = []
for _ in range(N):
    x, y, d, g = map(int, input().split())
    solve(x, y, d, g)

# 출발점, 도착점, 선분에 대한 정보는 일정하게.[sx, sy, ex, ey]
