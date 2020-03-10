from itertools import combinations
from copy import deepcopy

def game(archer, e):
    count = 0 
    while True:
        # enemy 
        deleteList = dict()
        for ai, aj in archer:
            idx, target = -1, [-1, -1, N+M]
            for i, ee in enumerate(e):
                tempD = abs(ai-ee[0]) + abs(aj-ee[1])
                # 공격거리 안이고, 기존 타겟보다 가까운경우
                if tempD <= D and tempD < target[2]:
                    idx, target[0], target[1], target[2] = i, ee[0], ee[1], tempD
                # 공격거리 안, 기존 타겟과 같은 거리, 왼쪽에 있는 경우
                elif tempD <= D and tempD == target[2] and target[1] > ee[1]:
                    idx, target[0], target[1], target[2] = i, ee[0], ee[1], tempD
            if target[0] != -1 and target[1] != -1:
                deleteList.update({idx: True})
        li = list(deleteList.keys())
        li.sort()
        li.reverse()
        count += len(li)
        for i in li:
            e.pop(i)
        # 아래로 내리는 과정.
        tempEnemy = []
        for ee in e:
            if ee[0]+1 == N:
                continue
            else:
                tempEnemy.append([ee[0]+1, ee[1]])
        e = deepcopy(tempEnemy)
        deleteList.clear()
        if len(e) == 0:
            break
    return count
        

enemy, map_ = [], []
N, M, D = map(int, input().split())
for i in range(N):  
    temp = list(map(int, input().split()))
    for j, value in enumerate(temp):
        if value == 1:
            enemy.append([i, j])
    map_.append(temp)

tail = list(range(M))
posPerm = combinations(tail, 3)
ans = 0
for pos in posPerm:
    archer = []
    for j in pos:
        archer.append([N, j])
    val = game(archer, deepcopy(enemy))
    ans = max(ans, val)
print(ans)