from itertools import product
# 研究用
R, C = map(int,input().split())
lines = []
for r in range(R):
    line = list(map(int,input().split()))
    lines.append(line)
lines = list(zip(*lines))
ans = 0
for p in product((0,1),repeat=R):
    sm = 0
    for line in lines:
        cnt = 0
        for r in range(R):
            if p[r] == line[r]:
                cnt += 1
        sm += max(cnt, R-cnt)
    ans = max(ans, sm)
print (ans)
