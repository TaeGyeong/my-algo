import itertools
def cal(k):
    hap = 0
    for h in house: # 집
        temp = 10000 
        for j in k: # 치킨집
            temp = min(temp, abs(h[0]-j[0])+abs(h[1]-j[1]))
        hap += temp
    return hap

def dfs(cnt):
    global ans
    if cnt == M+1:
        return
    p = itertools.combinations(chicken, cnt)
    for k in p: # 폐업외에 치킨집들
        ans = min(ans, cal(k))

N, M = map(int, input().split())
house, chicken = [], []
l = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if l[i][j] == 2:
            chicken.append([i, j])
        elif l[i][j] == 1:
            house.append([i, j])
ans = 100000
dfs(M)
print(ans)