import itertools
N = int(input())
counsle = [list(map(int, input().split())) for _ in range(N)]
maxValue = 0
def dfs(arr, sum, cnt):
    global maxValue
    tempArr = arr[:]
    if cnt == N:
        maxValue = max(sum, maxValue)
        return
    if arr[cnt] or cnt + counsle[cnt][0] > N:
        dfs(arr, sum, cnt + 1)
    else:
        for k in range(cnt, cnt + counsle[cnt][0]):
            tempArr[k] = True
        dfs(tempArr, sum + counsle[cnt][1], cnt + 1)
        dfs(arr, sum, cnt + 1)
arr = [False] * N
dfs(arr, 0, 0)
print(maxValue)