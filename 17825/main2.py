def turn_reverse_clock(i, k):
    for ni in range(i, N+1, i):
        for _ in range(k):
            plate[ni-1].append(plate[ni-1].pop(0))

def turn_clock(i, k):
    for ni in range(i, N+1, i):
        for _ in range(k):
            plate[ni-1].insert(0, plate[ni-1].pop())

def find_same_num():
    rtn = set()
    for i in range(N):
        for j in range(M):
            if plate[i][j]:
                pos = check(i, j)
                if pos:
                    rtn.add((i, j))
                for a, b, in pos:
                    rtn.add((a, b))
    return rtn

def check(i, j):
    rtn = []

    ni, nj = i, j-1
    if nj == -1:
        nj = M-1
    if plate[ni][nj] == plate[i][j]:
        rtn.append([ni, nj])

    ni, nj = i, j+1
    if nj == M:
        nj = 0
    if plate[ni][nj] == plate[i][j]:
        rtn.append([ni, nj])

    ni, nj = i-1, j
    if ni != -1:
        if plate[ni][nj] == plate[i][j]:
            rtn.append([ni, nj])

    ni, nj = i+1, j
    if ni != N:
        if plate[ni][nj] == plate[i][j]:
            rtn.append([ni, nj])
    return rtn

def remove_num(pos):
    for i, j in pos:
        plate[i][j] = 0

def find_avr_plus_minus_1():
    l = len([1 for i in range(N) for j in range(M) if plate[i][j]])
    avr = sum(map(sum, plate))/(l if l else 1)
    for i in range(N):
        for j in range(M):
            if plate[i][j] and plate[i][j]:
                plate[i][j] -= 1
            elif plate[i][j] and plate[i][j]:
                plate[i][j] += 1

N, M, T = map(int, input().split())
plate = [list(map(int, input().split())) for _ in range(N)]

for _ in range(T):
    i, d, k = map(int, input().split())
    if d:
        turn_reverse_clock(i, k)
    else:
        turn_clock(i, k)
    pos = find_same_num()
    if pos:
        remove_num(pos)
    else:
        find_avr_plus_minus_1()

print(sum(map(sum, plate)))