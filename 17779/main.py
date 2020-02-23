def sum_1D(graph, x, y, d1, d2):
    sum_1 = 0
    for i in range(x+d1):
        for j in range(y+1):
            sum_1 = sum_1 + graph[i][j]
    t = -1
    for i in range(x, x+d1):
        t = t + 1
        for j in range(y-t, y+1):
            sum_1 = sum_1 - graph[i][j]
    return sum_1

def sum_2D(graph, x, y, d1, d2):
    sum_2 = 0 
    for i in range(x+d2+1):
        for j in range(y+1, N):
            sum_2 += graph[i][j]
    t = 0
    for i in range(x+1, x+d2+1):
        t = t+1
        for j in range(y+1, y+1+t):
            sum_2 -= graph[i][j]
    return sum_2

def sum_3D(graph, x, y, d1, d2):
    sum_3 = 0
    for i in range(x+d1, N):
        for j in range(y-d1+d2):
            sum_3 += graph[i][j]
    t = -1
    for i in range(x+d1, x+d1+d2+1):
        t = t + 1
        for j in range(y-d1+t, y-d1+d2):
            sum_3 -= graph[i][j]
    return sum_3

def sum_4D(graph, x, y, d1, d2):
    sum_4 = 0
    for i in range(x+d2+1, N):
        for j in range(y-d1+d2, N):
            sum_4 += graph[i][j]
    t = -1
    for i in range(x+d2+1, x+d2+d1+1):
        t += 1
        for j in range(y-d1+d2, y+d2-t):
            sum_4 -= graph[i][j]
    return sum_4
    

N = int(input())
city, totalsum = [], 0
for _ in range(N):
    temp = list(map(int, input().split()))
    totalsum += sum(temp)
    city.append(temp)

minValue = float('inf')
for x in range(0, N-2):
    for y in range(1, N-1):
        for d1 in range(1, y+1):
            for d2 in range(1, N-y):
                try:
                    district = []
                    district.append(sum_1D(city, x, y, d1, d2))
                    district.append(sum_2D(city, x, y, d1, d2))
                    district.append(sum_3D(city, x, y, d1, d2))
                    district.append(sum_4D(city, x, y, d1, d2))
                    district.append(totalsum - sum(district))
                    district.sort()
                    if minValue > district[-1] - district[0]:
                        minValue = district[-1] - district[0]
                except:
                    break
print(minValue)

