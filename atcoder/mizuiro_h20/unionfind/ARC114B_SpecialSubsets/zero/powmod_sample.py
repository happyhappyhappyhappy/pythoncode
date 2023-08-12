MOD = 10**2
N = 20
p = [1]
for n in range(N):
    p.append((p[-1]*2)%MOD)

for n in range(N):
    print(f"{(p[n]-1)%MOD}")
