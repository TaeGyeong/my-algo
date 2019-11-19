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

def rotate(idx, direction):
    if direction == '-':
        li = [0, 0, 0, 0, 0, 0]
        for _ in range(3):
            col = 0
            for i in range(3):
                li[i] = cube[idx][col]
    elif direction == '+':
        pass
for _ in range(int(input())):
    for _ in range(int(input())):
        move = input()
        
        solve(input())
        print(cube[0][1]+cube[0][2]+cube[0][3])
        print(cube[0][4]+cube[0][5]+cube[0][6])
        print(cube[0][7]+cube[0][8]+cube[0][9])
        
        