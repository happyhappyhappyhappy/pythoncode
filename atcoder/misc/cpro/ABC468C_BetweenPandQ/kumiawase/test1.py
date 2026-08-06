from itertools import permutations

Y=10
X = [x+1 for x in range(Y)]

print(X)
for x in permutations(X):
    print(x)
