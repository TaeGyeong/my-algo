import itertools 

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr2 = []
for i in range(N):
    arr2.append(i)
p = itertools.combinations(arr2, N//2) 

def calculate(team):
    value = 0
    for i in range(len(team)-1):
        for j in range(i+1, len(team)):
            x, y = team[i], team[j]
            value += arr[x][y]
            value += arr[y][x]
    return value

def solve(case1):
    case2 = tuple(set(arr2) - set(case1))
    a = calculate(case1)
    b = calculate(case2)
    return abs(a-b)

minVal = 100000000
for case in p:
    minVal = min(minVal, solve(case))
print(minVal)