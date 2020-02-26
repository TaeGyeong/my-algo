r, c, k = map(int, input().split())
A = []
for _ in range(3):
    b = list(map(int, input().split()))
    A.append(b)
ans=0
while A[r][c] != k:
    ans += 1
    col, row = len(A), len(A[0]) # 행, 열
    if col >= row:
        for i in range(col):
            temp = [0 for _ in range(100)]
            for val in A[i]:
                temp[val] += 1
            
print(ans)


'''
R 연산: 배열 A의 모든 행에 대해서 정렬을 수행한다. 행의 개수 ≥ 열의 개수인 경우에 적용된다.
C 연산: 배열 A의 모든 열에 대해서 정렬을 수행한다. 행의 개수 < 열의 개수인 경우에 적용된다.
'''