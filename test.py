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
cube.append(temp0)
print(cube)