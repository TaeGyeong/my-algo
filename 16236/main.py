def helpCheck():
    for i in range(N):
        for j in range(N):
            if space[i][j] == 9:
                pass
            if space[i][j] < sharkSize: # 자기보다 작은 사이즈가 있는 경우
                return False
    return True # 먹을 수 있는 물고기가 없어 헬프하느 경우

# time check
# 상어가 한칸 이동하는데 1초


N = int(input())
space = []
babyShark = list()
sharkSize = 2
for i in range(N):
    temp = list(map(int, input().split()))
    try:
        j = temp.index(9)
        babyShark.append(i)
        babyShark.append(j)
    except:
        pass
    space.append(temp)