n = int(input())
nul = [[0]*n for i in range(n)]
x,y = 0,0
for i in range(1, n**2+1):
    nul[x][y] = i
    if x<=y+1 and x+y<n-1: y+=1
    elif x<y:
        x+=1
    elif x+y>=n:
        y-=1
    elif x>=y:
        x-=1
for i in range(n):
    print(*nul[i])