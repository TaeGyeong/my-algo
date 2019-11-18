import itertools
N = input()
A = list(map(int, input().split()))
sign = list(map(int, input().split()))
signList = []
max, min = -1000000000, 1000000000

def cal(a, b, c):
    if c == '+':
        return a+b
    elif c == '-':
        return a-b
    elif c == '*':
        return a * b
    else:
        if a < 0:
            return -(-a//b)
        return a//b
def calculate(case):
    idx, temp = 0, 'None'
    for s in case:
        if temp == 'None':
            temp = cal(A[idx], A[idx+1], s)
            idx += 1
        else:
            temp = cal(temp, A[idx+1], s)
            idx += 1
    if temp > 1000000000:
        temp = 1000000000
    elif temp < -1000000000:
        temp = -1000000000
    return temp
            
for i in range(len(sign)):
    if i==0:
        for _ in range(sign[i]):
            signList.append('+')
    elif i==1:
        for _ in range(sign[i]):
            signList.append('-')
    elif i==2:
        for _ in range(sign[i]):
            signList.append('*')
    elif i==3:
        for _ in range(sign[i]):
            signList.append('/')
p = itertools.permutations(signList)
for case in p:
    val = calculate(case)
    if max < val:
        max = val
    if min > val:
        min = val
print(max)
print(min)