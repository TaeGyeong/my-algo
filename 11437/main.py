def dfs(fr, cnt):
    global depth, tree, parent
    cnt += 1
    depth[fr] = cnt
    for ne in tree[fr]:
        if depth[ne] == 0:
            dfs(ne, cnt)
            parent[ne] = fr
    
def solve(a, depth_a, b, depth_b):
    global parent
    if depth_a > depth_b:
        while depth_a != depth_b:
            depth_a -= 1
            a = parent[a]
    elif depth_a < depth_b:
        while depth_a != depth_b:
            depth_b -= 1
            b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
M = int(input())
depth, parent = [0] * (N+1), [0] * (N+1)
dfs(1, 1)
for _ in range(M):
    a, b = map(int, input().split())
    same = solve(a, depth[a], b, depth[b])
    print(same)