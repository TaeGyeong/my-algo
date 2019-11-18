N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

needSuper = 0
for i in range(len(A)):
    if A[i] <= B:
        A[i] = 0
        needSuper += 1
        continue
    else:
        A[i] -= B
        needSuper += 1
    if A[i] % C == 0:
        needSuper += A[i] // C
    else:
        needSuper += (A[i] // C) + 1
print(needSuper)