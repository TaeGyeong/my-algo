import collections 
N = int(input()) # map size
K = int(input()) # number of apple
apple = [tuple(map(int, input().split())) for _ in range(K)] # 사과 위치.
L = int(input()) # number of direction.
tNdir = [tuple(map(str, input().split())) for _ in range(L)] # 
# L = left, D = right

dirX = (0, 1, 0, -1) # 오른쪽, 아래, 왼쪽, 위.
dirY = (1, 0, -1, 0)
snakes = collections.deque([[1, 1]])

def start():
    direction, time = 0, 0
    while True:
        for i in range(L):
            if time == int(tNdir[i][0]):
                if tNdir[i][1] == 'D':
                    direction = (direction + 1) % 4
                elif tNdir[i][1] == 'L':
                    direction = (direction - 1) % 4
        [x, y] = snakes[0]
        nx = x + dirX[direction]
        ny = y + dirY[direction]
        if [nx, ny] in snakes:
            time += 1
            break
        if nx > N or ny > N or nx <= 0 or ny <= 0:
            time += 1
            break
        flag, index = True, 0
        for idx in range(len(apple)):
            if (nx, ny) == apple[idx]:
                flag = False
                index = idx     
        if flag: # 사과가 없으면
            snakes.pop()
            snakes.appendleft([nx, ny])
        else: # 사과가 있으면
            del apple[index]
            snakes.appendleft([nx, ny])
        time += 1
    print(time)
start()
        



