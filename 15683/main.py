import copy
N, M = map(int, input().split())
map_ = [list(map(int, input().split())) for _ in range(N)]
# 0 = 위, 1 = 왼쪽, 2 = 오른쪽, 3 = 아래
cctv_1 = [(0, ), (1, ), (2, ), (3, )]
cctv_2 = [(1, 2), (0, 3)]
cctv_3 = [(0, 2),  (2, 3), (1, 3), (0, 1)]
cctv_4 = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
minValue = N * M

def makeMap(li):
    tempMap = copy.deepcopy(map_)
    for i in range(len(cctvList)):
        x, y = cctvList[i]
        for direction in li[i]:
            if direction == 0: # 위
                for dx in range(x-1, -1, -1):
                    if tempMap[dx][y] == 6:
                        break 
                    tempMap[dx][y] = '#'
            elif direction == 1: # 왼쪽
                for dy in range(y-1, -1, -1):
                    if tempMap[x][dy] == 6:
                        break 
                    tempMap[x][dy] = '#'
            elif direction == 2: # 오른쪽
                for dy in range(y+1, M):
                    if tempMap[x][dy] == 6:
                        break 
                    tempMap[x][dy] = '#'
            elif direction == 3: # 아래
                for dx in range(x+1, N):
                    if tempMap[dx][y] == 6:
                        break 
                    tempMap[dx][y] = '#'
    count = 0
    for i in range(N):
        for j in range(M):
            if tempMap[i][j] == 0:
                count += 1
    return count

def dfs(cnt, li):
    # 모든 cctv의 방향이 정해졌을 때.
    global minValue
    if cnt == len(cctvList):
        minValue = min(makeMap(li), minValue)
        return
    x, y = cctvList[cnt]
    if map_[x][y] == 1:
        for i in cctv_1:
            temp = li[:]
            temp.append(i)
            dfs(cnt+1, temp)
    elif map_[x][y] == 2:
        for i, j in cctv_2:
            temp = li[:]
            temp.append((i, j))
            dfs(cnt+1, temp)
    elif map_[x][y] == 3:
        for i, j in cctv_3:
            temp = li[:]
            temp.append((i, j))
            dfs(cnt+1, temp)
    elif map_[x][y] == 4:
        for i, j, z in cctv_4:
            temp = li[:]
            temp.append((i, j, z))
            dfs(cnt+1, temp)
    elif map_[x][y] == 5:
        temp = li[:]
        temp.append((0, 1, 2, 3))
        dfs(cnt+1, temp)
    
cctvList = []
for i in range(N):
    for j in range(M):
        if map_[i][j] != 0 and map_[i][j] != 6:
            k = tuple((i, j))
            cctvList.append(k)
dfs(0, list())
print(minValue)