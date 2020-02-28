stack = [[[] for _ in range(4)] for _ in range(4)]

stack[1][1].append(1)
stack[1][1].append(2)
stack[1][1].append(3)
print(stack[1][1])