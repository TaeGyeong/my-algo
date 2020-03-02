import copy
cube = list()
color = ['w', 'y', 'r', 'o', 'g', 'b']
temp0 = list()
for i in range(6):
    temp1 = list()
    for j in range(3):
        temp2 = list()
        for z in range(3):
            temp2.append(color[i])
        temp1.append(temp2)
    temp0.append(temp1)
cube.append(temp0) # make cube 위 아래 앞 뒤 왼 오른
color = ['U', 'D', 'F', 'B', 'L', 'R']
def rotate(idx, direction):
    li = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    if direction == '-': # 반시계
        for i in range(3):
            for j in range(3):
                li[2-j][i] = cube[idx][i][j]
        cube[idx] = copy.deepcopy(li)
    elif direction == '+': # 시계
        for i in range(3):
            for j in range(3):
                li[j][2-i] = cube[idx][i][j]
        cube[idx] = copy.deepcopy(li)
        
# 위 0 / 아래 1 / 앞 2 / 뒤 3 / 왼 4 / 오른 5
def rotateOther(idx):
    if idx == 0: # 윗면 시계방향
        # p = 정면
        p = list([cube[2][0][0], cube[2][0][1], cube[2][0][2]])
        cube[2][0][0], cube[2][0][1], cube[2][0][2] = \
            cube[5][0][0], cube[5][0][1], cube[5][0][2]
        cube[5][0][0], cube[5][0][1], cube[5][0][2] = \
            cube[3][0][0], cube[3][0][1], cube[3][0][2]
        cube[3][0][0], cube[3][0][1], cube[3][0][2] = \
            cube[4][0][2], cube[4][0][1], cube[4][0][0]
        cube[4][0] = p
    elif idx == 1: # 아랫면 시계 방향
        # p = 정면
        p = list([cube[2][2][0], cube[2][2][1], cube[2][2][2]])
        cube[2][2][0], cube[2][2][1], cube[2][2][2] = \
            cube[4][2][0], cube[4][2][1], cube[4][2][2]
        cube[4][2][0], cube[4][2][1], cube[4][2][2] = \
            cube[3][2][2], cube[3][2][1], cube[3][2][0]
        cube[3][2][0], cube[3][2][1], cube[3][2][2] = \
            cube[5][2][0], cube[5][2][1], cube[5][2][2]
        cube[5][2] = p
    elif idx == 2: # 정면 시계방향
        # p = 윗면
        p = list([cube[0][2][0], cube[0][2][1], cube[0][2][2]])
        cube[0][2][0], cube[0][2][1], cube[0][2][2] = \
            cube[4][2][2], cube[4][1][2], cube[4][0][2]
        cube[4][0][2], cube[4][1][2], cube[4][2][2] = \
            cube[3][0][0], cube[3][0][1], cube[3][0][2]
        
        # 이하생략. 노가다.
        
def solve(case):
    idx, c = color.index(case[0]), case[1]
    rotate(idx, c)
    if c=='+': # 시계방향일 때는 한번. 반시계는 3번 돌리면댐;
        rotateOther(idx)
    else:
        for _ in range(3):
            rotateOther(idx)

for _ in range(int(input())):
    for _ in range(int(input())):
        move = input()
        solve(move)
    print(cube[0][0][0]+cube[0][0][1]+cube[0][0][2])
    print(cube[0][1][0]+cube[0][1][1]+cube[0][1][2])
    print(cube[0][2][0]+cube[0][2][1]+cube[0][2][2])
        