from itertools import permutations

N = int(input()) # 이닝 수.
innings = [list(map(int, input().split())) for _ in range(N)] 

result = 0 
for perm in permutations(range(1, 9)):
    tasoon = list(perm)[:3] + [0] + list(perm)[3:]
    taza = 0
    score = 0
    for inning in innings:
        b1, b2, b3 = 0, 0, 0
        out = 0
        while True:
            hit = inning[tasoon[taza]]
            if hit == 0:
                out += 1
            elif hit == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif hit == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif hit == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            elif hit == 4:
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0
            taza = (taza + 1) % 9
            if out >= 3:
                break
    if score > result:
        result = score
print(result)
