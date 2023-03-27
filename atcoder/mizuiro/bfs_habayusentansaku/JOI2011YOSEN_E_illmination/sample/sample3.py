from collections import deque
inf = 10**10

w,h = map(int,input().split())

field = [[ 0 for j in range(w+2)] for k in range(h+2)]
visited = [[ 0 for j in range(w+2)] for k in range(h+2)]

for i in range(h):
    field[i+1][1:w+1]=map(int,input().split())

odd_move = [[-1,1],[0,1],[1,1],[1,0],[0,-1],[-1,0]]
even_move = [[-1,0],[0,1],[1,0],[1,-1],[0,-1],[-1,-1]]

Q = deque([])
Q.append([0,0])
visited[0][0]=1

collision = 0
while Q:
    y,x = Q.popleft()
    if y % 2 == 1:
        dhdw = odd_move
    else:
        dhdw = even_move
    for j,k in dhdw:
        ny,nx = y+j,x+k
        if ny < 0 or nx < 0 or h+2 <= ny or w+2 <= nx:
            continue
        elif field[ny][nx] == 1:
            collision = collision+1
            continue
        elif visited[ny][nx] == 1:
            continue
        else:
            visited[ny][nx]=1
            Q.append([ny,nx])
print(collision)
