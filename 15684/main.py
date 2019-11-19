def check(a):
    for i in range(1, M+1):
        start = end = i
        for j in range(1, N+1):
            if a[j][end]:
                end += 1
                continue
            if end == 1: continue
            if not a[j][end]:
                if a[j][end-1]:
                    end -= 1
        if start != end:
            return False
    return True

def go(x, y, cnt, a):
    global answer
    if y == M+1:
        x += 1
        y = 1
    if cnt == 3 or (x==N and y==M):
        if check(a):
            answer = min(cnt, answer)
        return
    go(x, y+1, cnt, a)

    if(y==M or a[x][y] or (y!=1 and a[x][y-1]) or a[x][y+1]):
        return
    a[x][y] = True
    go(x, y+1, cnt+1, a)
    a[x][y] = False

N, M, H = map(int, input().split()); answer = 4
a = [[False]* (N+1) for _ in range(M+2)]
for _ in range(M):
    x, y = map(int, input().split())
    a[x][y] = True
go(1, 1, 0, a)
if answer == 4:
    answer -= 1
print(answer)

