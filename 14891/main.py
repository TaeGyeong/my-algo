import collections
wheels = [collections.deque(input()) for _ in range(4)]
K = int(input())
move = [list(map(int, input().split())) for _ in range(K)]

def beforeCheck(i):
    one = False
    if i-1 == -1:
        pass
    else:
        if wheels[i-1][2] == wheels[i][6]:
            pass
        else:
            one = True
    return one
def afterCheck(i):
    two = False
    if i+1 == 4:
        pass
    else:
        if wheels[i+1][6] == wheels[i][2]:
            pass
        else:
            two = True 
    return two

def solve(i, direction, cnt=0):
    before, after = beforeCheck(i), afterCheck(i)    
    if direction == 1: # 시계방향
        temp = wheels[i].pop()
        wheels[i].appendleft(temp)
    else: # 반시계방향
        temp = wheels[i].popleft()
        wheels[i].append(temp)
    if cnt==0:
        if before:
            solve(i-1, (-1)*direction, cnt-1)
        if after:
            solve(i+1, (-1)*direction, cnt+1)
    elif cnt < 0:
        if before:
            solve(i-1, (-1)*direction, cnt-1)
    else:
        if after:
            solve(i+1, (-1)*direction, cnt+1)
        
for idx, direction in move:
    solve(idx-1, direction)

answer, value = 0, 1
for wheel in wheels:
    if wheel[0] == '1':
        answer = answer + value
    value *= 2
print(answer)