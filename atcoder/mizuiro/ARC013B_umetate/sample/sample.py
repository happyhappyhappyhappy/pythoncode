from functools import reduce
from operator import and_

mapdict = {(i, j): c for i in range(10) for j, c in enumerate(input())}

def dfs(start):
    stack = [start]
    while stack:
        i, j = stack.pop()
        current = mapdict.get((i, j), 'v')
        if current == 'v':
            continue
        if current == 'x':
            yield (i, j)
            continue
        mapdict[i, j] = 'v'
        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
        stack.extend((i+di, j+dj) for di, dj in dirs)

surroundings = []
for coord in mapdict:
    if mapdict[coord] == 'o':
        surroundings.append(set(dfs(coord)))

print('YES' if len(reduce(and_, surroundings)) else 'NO')
