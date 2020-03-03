def go():
    for n in range(1, K+1):
        i, j = pos[n]
        ni, nj, dir[n]

N, K = map(int, input().split())
board_info = [list(map(int, input().split())) for _ in range(N)]
board = [[[] for _ in range(N)] for _ in range(N)]
pos = [-1]
dir = [-1]
di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

for n in range(1, K+1):
    i, j, d = map(int, input().split())
    i-=1; j-=1; d-=1
    board[i][j].append(n)
    pos.append([i, j])
    dir.append(d)
turn = 0
while True:
    turn += 1
    if turn == 1001:
        print(-1)
        break
    if go():
        print(turn)
        break