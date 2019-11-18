N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
visit = [[False] * M for _ in range(N)]
dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)
answer = 0

def dfs(x, y, sum, cnt):
    global answer, visit
    visit[x][y] = True
    if cnt == 3:
        answer = max(answer, sum)
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if visit[nx][ny]: 
            continue
        dfs(nx, ny, sum + paper[nx][ny], cnt + 1)
        visit[nx][ny] = False

def shape1(x, y): # ㅗ
    global answer
    if x-1 >= 0 and y+2 < M:
        answer = max(answer, paper[x][y] + paper[x][y+1] + \
             paper[x][y+2] + paper[x-1][y+1])

def shape2(x, y): # ㅜ
    global answer
    if x+1 < N and y+2 < M: 
        answer = max(answer, paper[x][y] + paper[x][y+1] + \
            paper[x][y+2] + paper[x+1][y+1])

def shape3(x, y): # ㅏ
    global answer
    if x+2 < N and y+1 < M: 
        answer = max(answer, paper[x][y] + paper[x+1][y] + \
            paper[x+2][y] + paper[x+1][y+1])

def shape4(x, y): # ㅓ
    global answer
    if x+1 < N and x-1 >= 0 and y+1 < M:
        answer = max(answer, paper[x][y] + paper[x-1][y+1] + \
            paper[x][y+1] + paper[x+1][y+1])

def findMax():
    global visit
    for i in range(N):
        for j in range(M):
            dfs(i, j, paper[i][j], 0)
            visit[i][j] = False
            shape1(i, j)
            shape2(i, j)
            shape3(i, j)
            shape4(i, j)
    print(answer)
findMax()

    