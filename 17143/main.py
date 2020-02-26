r, c, m = map(int, input().split())
a = [[[0, 0, 0] for _ in range(c)] for _ in range(r)]
for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    a[x-1][y-1] = [s, d-1, z]
dx, dy, ans = (-1, 1, 0, 0), (0, 0, 1, -1), 0

for t in range(c):
    b = [[[0, 0, 0] for _ in range(c)] for _ in range(r)]
    for i in range(r):
        _, _, z = a[i][t]
        if z:
            ans += z
            a[i][t] = [0, 0, 0]
            break
    for i in range(r):
        for j in range(c):
            s, d, z = a[i][j]
            if z:
                if d < 2:
                    ns, nd, ni = s % ((r-1) * 2), d, i
                    for _ in range(ns):
                        if ni == 0 and nd == 0:
                            nd = 1
                        if ni == r-1 and nd == 1:
                            nd = 0
                        ni += dx[nd]
                    _, _, bz = b[ni][j]
                    if z > bz:
                        b[ni][j] = [s, nd, z]
                else:
                    ns, nd, nj = s % ((c-1) * 2), d, j
                    for _ in range(ns):
                        if nj == 0 and nd == 3:
                            nd = 2
                        if nj == c-1 and nd == 2:
                            nd = 3
                        nj += dy[nd]
                    _, _, bz = b[i][nj]
                    if z > bz:
                        b[i][nj] = [s, nd, z]
                a[i][j] = [0, 0, 0]
    a = b[:]
print(ans)