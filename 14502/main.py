from itertools import combinations
from copy import deepcopy
n,m = map(int, input().strip().split())
arr = [list(map(int, input().split())) for _ in range(n)]
virus = []
safe = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            virus.append((i, j))
        elif arr[i][j] == 0:
            safe.append((i, j))

cnt_zeros = len(safe)-3
max_= 0

def spread(virus, wall):
    global max_, cnt_zeros

    left = cnt_zeros
    brr = deepcopy(arr)

    q = virus[::]
    for x, y in wall:
        brr[x][y] = 1 
    while q:
        x, y = q.pop(0)
        for dx, dy in (0, -1), (1, 0), (0, 1), (-1, 0):
            nx, ny = x+dx, y+dy
            if nx < 0 or nx>=n or ny<0 or ny>=m:
                continue
            if brr[nx][ny]:
                continue
            left -= 1
            brr[nx][ny] = 2
            q.append((nx, ny))

        if left <= max_:
            return
    max_ = left

for idx, wall in enumerate(combinations(safe, 3)):
    spread(virus, wall)

print(max_)
  

