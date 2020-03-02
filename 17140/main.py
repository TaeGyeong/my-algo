from collections import Counter

def endCheck():
    if time > 100:
        print(-1)
        return True
    if (A[r-1][c-1] == k):
        print(time)
        return True    
    return False
r, c, k  = map(int, input().split())
A = [[0 for _ in range(100)] for _ in range(100)]
for i in range(3):
    A[i][0], A[i][1], A[i][2] = map(int, input().split())
col, row = 3, 3 # 열 행
time = 0
# 순서 : 1. endcheck, 2. 연산, 3. time ++, 4. 타임 100 넘어가는지.
while True:
    if endCheck():
        break
    if row >= col:
        # R연산.
        maximum = 0 
        for i in range(row):
            result = Counter(A[i]).most_common()
            result.sort(key=lambda x: x[0])
            if result[0][0] == 0:
                result.pop(0)
            result.sort(key=lambda x: (x[1], x[0]))
            if len(result) > 50:
                # result 의 결과, A 의 길이가 100을 넘어가는 경우.
                col = 100
            else:
                # result 의 결과, A 의 결과가 100을 넘기지 않는 경우.
                col = max(col, len(result) * 2)
            idx = 0
            for a, b in result: # result 의 tuple 을 A 리스트에 넣기.
                    if idx == 100:
                        break
                    if a == 0:
                        continue
                    A[i][idx], A[i][idx+1] = a, b
                    idx += 2
            for t in range(idx, 100):
                    A[i][t] = 0
                    
    elif row < col:
        # C연산.
        for j in range(col):
            temp = []
            for i in range(row):
                temp.append(A[i][j])
            result = Counter(temp).most_common()
            result.sort(key=lambda x: x[0])
            if result[0][0] == 0:
                result.pop(0)
            result.sort(key=lambda x: (x[1], x[0]))
            if len(result) > 50:
                # result 의 결과, A 의 길이가 100을 넘어가는 경우.
                row = 100
            else:
                # result 의 결과, A 의 결과가 100을 넘기지 않는 경우.
                row = max(row, len(result) * 2)
            idx = 0
            for a, b in result: # result 의 tuple 을 A 리스트에 넣기.
                    if idx == 100:
                        break
                    if a == 0:
                        continue
                    A[idx][j], A[idx+1][j] = a, b
                    idx += 2
            for t in range(idx, 100):
                A[t][j] = 0
            
    time+=1

            
        

