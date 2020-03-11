n = 10
MAP = [list(map(int, input().split())) for _ in range(n)]
paper = [0] + [5]*5
answer = -1
total_one = sum(sum(m) for m in MAP)

def dfs(depth):
    global n, answer, total_one
    if 0 < answer <= depth:
        return
    if total_one == 0:
        if answer == -1 or answer > depth:
            answer = depth
        return
    
    for y in range(n):
        for x in range(n):
            if MAP[y][x]:
                break
        if MAP[y][x]:
            break

    if MAP[y][x]:
        for size in range(1, 6):
            if paper[size]:
                one2zero = []
                if isCoverable(y, x, size):
                    for next_y in range(y, y+size):
                        for next_x in range(x, x+size):
                            MAP[next_y][next_x] = 0
                            one2zero.append((next_y, next_x))
                    total_one -= size**(2)
                    paper[size] -= 1
                    dfs(depth+1)
                    paper[size] += 1
                    total_one += size**(2)
                    
                    for y_x in one2zero:
                        MAP[y_x[0]][y_x[1]] = 1

def isCoverable(y, x, size):
    global n
    for _y in range(y, y+size):
        for _x in range(x, x+size):
            if 0 <= _y < n and 0 <= _x < n:
                if MAP[_y][_x] == 0:
                    return False
            else:
                return False
    return True

dfs(0)
print(answer)