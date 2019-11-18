import collections
a = '01010101010'
p = collections.deque(a)
print(p)


# wheels = [collections.deque(input()) for _ in range(4)]

# K = int(input())
# move = [list(map(int, input().split())) for _ in range(K)]

# print(wheels)
# for wheel in wheels:
#     print(wheel)

# a = wheels[0].pop()
# print(a)
# print(wheels[0])