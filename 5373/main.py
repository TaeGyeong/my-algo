import collections
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
    cube.append(temp1)
                # 0    1    2    3    4    5
cubeDirection = ['U', 'D', 'F', 'B', 'L', 'R']
'''
    U
L   F   R   B
    D
'''
def rotateOtherClock(idx): # 시계방향으로 돌릴때 나머지부분 (반시계 = 3번 시계) 
    global cube
    if idx == 0: # 윗면돌리기
        one, two three = cube[2][0][0], cube[2][0][1], cube[2][0][2]
        # F(2) <- R(5)
        cube[2][0][0], cube[2][0][1], cube[2][0][2] = \
            cube[5][0][0], cube[5][0][1], cube[5][0][2]
        # R(5) <- B(3)
        cube[5][0][0], cube[5][0][1], cube[5][0][2] = \
            cube[3][0][0], cube[3][0][1], cube[3][0][2]
        # B(3) <- L(4)
        cube[3][0][0], cube[3][0][1], cube[3][0][2] = \
            cube[4][0][2], cube[4][0][1], cube[4][0][0]
        # L(4) <- F(2)
        cube[4][0][0], cube[4][0][1], cube[4][0][2] = \
            one, two, three
    elif idx == 1: # 아랫면 돌리기
        one, two three = cube[2][2][0], cube[2][2][1], cube[2][2][2]
        # F(2) <- R(5)
        cube[2][0][0], cube[2][0][1], cube[2][0][2] = \
            cube[5][0][0], cube[5][0][1], cube[5][0][2]
        # R(5) <- B(3)
        cube[5][0][0], cube[5][0][1], cube[5][0][2] = \
            cube[3][0][0], cube[3][0][1], cube[3][0][2]
        # B(3) <- L(4)
        cube[3][0][0], cube[3][0][1], cube[3][0][2] = \
            cube[4][0][2], cube[4][0][1], cube[4][0][0]
        # L(4) <- F(2)
        cube[4][0][0], cube[4][0][1], cube[4][0][2] = \
            one, two, three

def rotate(d, c):
    global cube
    idx = cubeDirection.index(d) # 어느 큐브를 중심으로 돌리는가
    temp = [[None]*3 for _ in range(3)]
    if c == '+': # 시계
        for i in range(3):
            for j in range(3):
                temp[j][3-i] = cube[idx][i][j]
        rotateOtherClock(idx)
    elif c == '-':
        for i in range(3):
            for j in range(3):
                temp[3-j][i] = cube[idx][i][j]
            rotateOtherClock(idx) # 반시계

def solve(move):
    direciton, clock = move[0], move[1]
    rotate(direciton, clock)

for _ in range(int(input())):
    for _ in range(int(input())):
        move = input() # direction, +/--
        solve(move)
        print(cube[0][0][0]+cube[0][0][1]+cube[0][0[2])
        print(cube[0][1][0]+cube[0][1][1]+cube[0][1][2])
        print(cube[0][2][0]+cube[0][2][1]+cube[0][2][2])
        
        