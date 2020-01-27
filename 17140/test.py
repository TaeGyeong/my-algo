from collections import Counter
A = [1, 2, 3, 1, 0, 0, 2, 3]
a = Counter(A).most_common()
a.sort(key=lambda x: x[0])
# if a[0][0] == 0:
#     a.pop(0)
print(a)


# from collections import Counter
# A = [[3, 2, 3], [1, 3, 4], [1, 1, 2], [2, 1, 4]]

# for j in range(3):
#     temp = []
#     for i in range(4):
#         temp.append(A[i][j])
#     result = Counter(temp).most_common()
#     print(result)

# for k in range(49, -1, -1):
#     print(k)

# print("---Counter()---")
# result = Counter(myList).most_common()
# print(result)

# #키 없이 카운트 한 값만 알아내고 싶으면
# print("---Counter().values()---")
# result = Counter(myList).values()
# print(result)