dice = list(map(int, input().split()))
path = [
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0],
    [10, 13, 16, 19, 25],
    [20, 22, 24, 25],
    [30, 28, 27, 26, 25],
    [25, 30, 35, 40, 0]
]

horse = [[0, 0], [0, 0], [0, 0], [0, 0]]
score = [0, 0, 0, 0]
answer = 0
def dfs(idx):
    if idx == 10:
        global answer
        answer = max(answer, sum(score))
        return answer

    move = dice[idx]

    for i in range(4):
        cur_path = horse[i][0]
        cur_pos = horse[i][1]

        if cur_pos == len(path[cur_path]) -1:
            continue

        next_path = cur_path
        next_pos = cur_pos + move
        
        if cur_path == 0:
            if next_pos == 5:
                next_path = 1
                next_pos = 0
            elif next_pos == 10:
                next_path = 2
                next_pos = 0
            elif next_pos == 15:
                next_path = 3
                next_pos = 0
            elif next_pos == 20:
                next_path = 4
                next_pos = 3
        elif cur_path < 4:
            if next_pos >= len(path[cur_path])-1:
                next_path = 4
                next_pos -= len(path[cur_path])-1

        if next_pos >= len(path[next_path]):
            next_pos = len(path[next_path])-1
        
        if path[next_path][next_pos] !=0:
            if [next_path, next_pos] in horse:
                continue
        horse[i][0], horse[i][1] = next_path, next_pos
        score[i] += path[next_path][next_pos]

        dfs(idx+1)
        
        horse[i][0], horse[i][1] = cur_path, cur_pos
        score[i] -= path[next_path][next_pos]

dfs(0)
print(answer)
        
        
            
            
            
    
