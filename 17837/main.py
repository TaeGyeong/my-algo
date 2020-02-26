N, K = map(int, input().split())
stack = [[[] for _ in range(N)] for _ in range(N)]
map_ = list()
for _ in range(N):
    temp = list(map(int, input().split()))
    map_.append(temp)
horse = list()
for i in range(K):
    tx, ty, direction = map(int, input().split())
    stack[tx-1][ty-1].append(i)
    horse.append([tx-1, ty-1, direction])
print(map_)
print(stack)
print(horse)