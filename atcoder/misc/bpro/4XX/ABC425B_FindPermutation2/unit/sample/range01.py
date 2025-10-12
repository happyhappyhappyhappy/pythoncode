from itertools import permutations

perm=permutations

for x in perm([j+1 for j in range(3)]):
    print(x)
