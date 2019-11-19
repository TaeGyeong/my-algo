from itertools import product,combinations as cm

def chk_sadari(sa,sa_added):
    for col in range(1,n+1):
        go = col
        for row in range(1,h+1):
            if sa[row][go]==1 or sa_added[row][go]==1:
                go+=1
            elif sa[row][go-1]==1 or sa_added[row][go-1]==1:
                go-=1
        if go != col:
            return False
    return True

n,m,h=map(int,input().split())
sadari = [[0]*(n+1) for _ in range(h+1)]    # 1 index

# 가로선이 없는 경우 예외처리
if m==0:
    print(0)
    exit(1)

# 사다리 입력정보
for _ in range(m):
    a,b=map(int,input().split())
    sadari[a][b]=1

if chk_sadari(sadari,sadari):
    print(0)
    exit(1)

for i in range(1,3+1):
    kFlag = False
    for now_line_list in cm(product(range(1,h+1),range(1,n)),i):  # 행렬의 인덱스를 1~h개를 뽑는 조합
        if kFlag:
            break
        sadari_added = [[0]*(n+1) for _ in range(h+1)]
        # 뽑은 조합들로 사다리에 가로선 추가하기
        flag = False
        for pos in now_line_list:
            x,y=pos
            if sadari[x][y-1]==1 or sadari_added[x][y-1]==1 or sadari[x][y+1]==1 or sadari_added[x][y+1]==1 or sadari[x][y]==1:
                flag=False
                break
            sadari_added[x][y]=1
            flag= True
        if flag and chk_sadari(sadari,sadari_added):
            print(i)
            kFlag = True
print(-1)