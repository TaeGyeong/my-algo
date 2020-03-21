from itertools import permutations
from collections import deque
from copy import deepcopy

dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)

N, M, K = map(int, input().split())
map_ = [list(map(int, input().split())) for _ in range(N)]
calculation = []
for _ in range(K):
    calculation.append(list(map(int, input().split())))

def rotate(rotList, m):
    x, y, z = rotList[0]-1, rotList[1]-1, rotList[2]
    for tz in range(1, z+1):
        count = 4*(2*tz-1) + 4
        tx, ty = x-tz, y-tz-1
        temp, direction = deque(), 0
        for _ in range(count):
            tx, ty = tx + dx[direction], ty + dy[direction]
            temp.append(m[tx][ty])
            if tx == x-tz and ty == y+tz:
                direction += 1
            elif tx == x+tz and ty == y+tz:
                direction += 1
            elif tx == x+tz and ty == y-tz:
                direction += 1
        tempVal = temp.pop()
        temp.appendleft(tempVal)     
        
        tx, ty = x-tz, y-tz-1
        direction = 0
        for _ in range(count):
            tx, ty = tx + dx[direction], ty + dy[direction]
            m[tx][ty] = temp.popleft()
            if tx == x-tz and ty == y+tz:
                direction += 1
            elif tx == x+tz and ty == y+tz:
                direction += 1
            elif tx == x+tz and ty == y-tz:
                direction += 1

def go(li):
    global answer, map_
    tempMap = [[a for a in e] for e in map_]
    for rot in li: # rot = 연산
        rotate(rot, tempMap)
    
    for idx in range(N):
        answer = min(answer, sum(tempMap[idx]))


permu = permutations(calculation)
answer = 9 * M + 1
for perm in permu:
    go(perm)
print(answer)
    
