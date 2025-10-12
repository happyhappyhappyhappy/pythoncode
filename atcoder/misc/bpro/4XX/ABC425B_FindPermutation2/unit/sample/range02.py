from itertools import permutations
N=3
P=permutations([j+1 for j in range(N)])
print(type(P))
for x_tuple in P:
    x = list(x_tuple)
    print(x)
