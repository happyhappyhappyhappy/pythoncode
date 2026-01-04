N,M=map(int,input().split())
S=[input() for _ in range(N)]

grid_set=set()
for i in range(N-M+1):
  for j in range(N-M+1):
    grid = tuple(S[ii][j:j+M] for ii in range(i,i+M))
    grid_set.add(grid)

print(f"{grid_set}")
print(len(grid_set))
