import itertools

n, m = map(int, input().split()) # n 은 지도 크기, m 은 경사로의 길이.
arr = [list(map(int, input().strip().split())) for _ in range(n)]

# 조건 : 
# 경사로를 놓기위해서는 두 스팟의 높이차이는 1
# 경사로는 겹쳐놓을 수가 없다. -> 경사로를 놓은 곳을 list 로 정리해서 비교한다.
def canGo(heights):
    current = heights[0]
    visit = list(0 for _ in range(n))
    
    for i, height in enumerate(heights):
        if current == height:
            continue
        # 높은곳
        elif current +1 == height:
            for j in range(i-1, i-1-m, -1):
                if j<0 or current != heights[j] or visit[j]==1:
                    return False
                visit[j] = 1
            current = height
        # 낮은곳
        elif current -1 == height:
            for j in range(i, i+m):
                if j >= n or current-1 != heights[j] or visit[j] ==1:
                    return False
                visit[j] = 1
            current = height
        # 높이차이가 1 초과
        else:
            return False
    return True

def solve():
    count = 0
    for i in range(n):
        if canGo(arr[i]):
            count += 1
    for j in range(n):
        path = []
        for i in range(n):
            path.append(arr[i][j])

        if canGo(path):
            count += 1
    print(count)

solve()
        

    