N, M = map(int, input().split())
r, c, d = map(int, input().split()) # 0북, 1동, 2남, 3서
map_ = [list(map(int, input().split())) for _ in range(N)]
# 빈칸은 0, 벽은 1.

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
# 왼쪽방향 = 북, 서 남, 동, 북, .. [0, 3, 2, 1, ]
def boolCheck(r, c, d):
    for i in range(1, 5):
        k = (d-i) % 4
        if map_[r+dx[k]][c+dy[k]] == 0:
            return 0, k, r+dx[k], c+dy[k]
        if i==4:
            return 1, d, r-dx[d], c-dy[d]
cleanCount = 0
while True:
    if map_[r][c] == 0: # 청소되어있지 않은 곳이면 청소.
        map_[r][c] = 2 # 2는 청소완료.
        cleanCount += 1
    endCheck, d, r, c = boolCheck(r, c, d)
    if endCheck:
        if map_[r][c] == 1:
            break
print(cleanCount)