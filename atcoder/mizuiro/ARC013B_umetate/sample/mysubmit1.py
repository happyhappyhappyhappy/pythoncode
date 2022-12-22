from functools import reduce
from operator import and_

mapdict = {(i,j) : c for i in range(10) for j,c in enumerate(input())}
print(mapdict)

def dfs(start):
    stack = [start]
    while stack :
        print("Now stack:{}".format(stack))
        i,j = stack.pop()
        current = mapdict.get((i,j),'v')
        if current == 'v':
            print("({},{})は「v」です".format(i,j))
            continue
        if current == 'x':
            yield(i,j)
            continue
        mapdict[i,j]='v'
        dirs = ((1,0),(-1,0),(0,1),(0,-1))
        stack.extend((i+di,j+dj) for di,dj in dirs)

surroundings=[]
for coord in mapdict:
    if mapdict[coord] == 'o':
        surroundings.append(set(dfs(coord)))

print("チェックする内容 : {}".format(reduce(and_, surroundings)))
if(len(reduce(and_, surroundings))):
    print("YES")
else:
    print("NO")
