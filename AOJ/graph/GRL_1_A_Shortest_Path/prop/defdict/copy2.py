from collections import defaultdict

d = defaultdict(lambda:float('inf'))
d[0]=3
# d[1]=2
d[2]=1

for j in range(0,3):
    x = d[j]
    if x != float('inf'):
        print(f"{j}->{x}")
    else:
        print(f"{j}->INF")
