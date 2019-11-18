def cycle(onepan, N, M, x, d, k):
    num = x-1
    while num <= N:
        if d==0:
            for _ in range(k):
                onepan[num].insert(0, onepan[num].pop())
        else:
            for _ in range(k):
                onepan[num].append(onepan[num].pop(0))
        num += x
    deleteList = list()
    flag = True
    for i in range(N):
        for j in range(M):
            if onepan[i][j] == 'x':
                continue
            if i == N-1 and j == M-1:
                if onepan[i][j] == onepan[i][j-1]:
                    flag = False
                    deleteList.append([i, j])
                    deleteList.append([i, j-1])
                if onepan[i][j] == onepan[i][0]:
                    flag = False
                    deleteList.append([i, j])
                    deleteList.append([i, 0])
            elif i == N-1:
                if onepan[i][j] == onepan[i][j-1]:
                    flag = False
                    deleteList.append([i, j])
                    deleteList.append([i, j-1])
                if onepan[i][j] == onepan[i][j+1]:
                    flag = False
                    deleteList.append([i, j])
                    deleteList.append([i, j+1])
            elif j == M-1:
                if onepan[i][j] == onepan[i][j-1]:
                    flag = False
                    deleteList.append([i, j])
                    deleteList.append([i, j-1])
                if onepan[i][j] == onepan[i][0]:
                    flag = False
                    deleteList.append([i, j])
                    deleteList.append([i, 0])
                if onepan[i+1][j] == onepan[i][j]:
                    flag = False
                    deleteList.append([i+1, j])
                    deleteList.append([i, j])
            else:
                if onepan[i][j] == onepan[i][j-1]:
                    flag = False
                    deleteList.append([i, j])
                    deleteList.append([i, j-1])
                if onepan[i][j] == onepan[i][j+1]:
                    flag = False
                    deleteList.append([i, j])
                    deleteList.append([i, j+1])
                if onepan[i+1][j] == onepan[i][j]:
                    flag = False
                    deleteList.append([i+1, j])
                    deleteList.append([i, j])

    for idx in range(len(deleteList)):
        ix = deleteList[idx][0]
        iy = deleteList[idx][1]
        onepan[ix][iy] = 'x'
    if flag:
        notSame(onepan, N, M)
        

def notSame(onepan, N, M):
    summation = 0 
    count = 0
    for i in range(N):
        for j in range(M):
            if onepan[i][j] == 'x':
                continue
            summation += onepan[i][j]
            count += 1
    avg = summation / count
    for i in range(N):
        for j in range(M):
            if onepan[i][j] == 'x':
                continue
            if onepan[i][j] > avg:
                onepan[i][j] -= 1
            elif onepan[i][j] < avg:
                onepan[i][j] += 1

N, M, T = map(int, input().split()) 
onepan = [list(map(int, input().split())) for _ in range(N)]
for _ in range(T):
    i, d, k = map(int, input().split())
    cycle(onepan, N, M, i, d, k)
sum_ = 0
for i in range(N):
    for j in range(M):
        if onepan[i][j] == 'x':
            continue
        sum_ += onepan[i][j]
print(sum_)