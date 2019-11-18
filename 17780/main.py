def go():
    for n in range(1, K+1):
        if is_root[n]:
            i, j = pos[n]
            ni, nj, dir[n] = next_pos_and_dir(n)
            if i==ni and j==nj: continue
            move_all(i, j, ni, nj)
            elements = board[i][j]
            board[i][j] = []
            if board_info[ni][nj] == 0 and not board[ni][nj]:
                board[ni][nj] += elements[:]
            elif board_info[ni][nj] == 0 and board[ni][nj]:
                board[ni][nj] += elements[:]
                is_root[n] = False
            elif board_info[ni][nj] == 1 and not board[ni][nj]:
                board[ni][nj] += elements[::-1]
                is_root[n] = False
                is_root[board[ni][nj][0]] = True
            elif board_info[ni][nj] == 1 and board[ni][nj]:
                board[ni][nj] += elements[::-1]
                is_root[n] = False
            if len(board[ni][nj]) >= 4:
                return True
    return False

def move_all(i, j, ni, nj):
    for n in board[i][j]:
        pos[n] = [ni, nj]

def next_pos_and_dir(n):
    (i, j), d = pos[n], dir[n]
    if check(i+di[d], j+dj[d]):
        i, j = i+di[d], j+dj[d]
    else:
        d ^= 1
        if check(i+di[d], j+dj[d]):
            i, j = i+di[d], j+dj[d]
    return (i, j, d)
    
def check(i, j):
    if not (0 <= i < N and 0 <= j < N): return False
    if board_info[i][j] == 2: return False
    return True

N, K = map(int, input().split())
board_info = [list(map(int, input().split())) for _ in range(N)]
board = [[[] for _ in range(N)] for _ in range(N)]
pos = [-1]
dir = [-1]
is_root = [True] * (K+1)
di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

for n in range(1, K+1):
    i, j, d = map(int, input().split())
    i -= 1; j-=1; d-=1
    board[i][j].append(n)
    pos.append([i, j])
    dir.append(d)

turn=0
while True:
    turn += 1
    if turn == 1001:
        print(-1)
        break
    if go():
        print(turn)
        break
