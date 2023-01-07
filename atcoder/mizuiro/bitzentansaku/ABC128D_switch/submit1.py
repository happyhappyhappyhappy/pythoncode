import sys
import pprint as pp
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

S,L = MI()
LtoS = []
for x in range(L):
    LtoS.append(LI())
tx,ty = MI()
for x in range(L):
    print(LtoS[x])

for y in range(2**S):
    print("---{}の場合---".format(y))
    for z in range(S):
        if (y>>z) & 1:
            print("{}のスイッチ押された".format(x))
        else:
            print("{}のスイッチ押されてない".format(x))
