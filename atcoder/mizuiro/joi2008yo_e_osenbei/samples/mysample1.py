from itertools import product
import sys,os

R,C = map(int,sys.stdin.readline().split())
print("R = {}  C = {}".format(R,C))
lines = list()
for r in range(0,R):
    nowline = list(map(int,sys.stdin.readline().split(" ")))
    lines.append(nowline)
lines = list(zip(*lines))
answer = 0
for bit in product((0,1),repeat=R):
    print("----- bit {} -----開始".format(bit))
    sm=0
    linecnt=0
    for line in lines:
        print("== {} line No.==".format(linecnt))
        cnt=0
        for r in range(R):
            print("bit[{}]={} ? line[{}]={}".\
                format(r,bit[r],r,line[r]))
            if bit[r] == line[r]:
                print("等しいので1追加します")
                cnt = cnt+1
            else:
                print("等しくないので何もしません")
        sm = sm + max(cnt,R-cnt)
        linecnt=linecnt+1
    print("bit = {} の時の表に出来る値は {} です\n\n".format(bit,sm))
    answer = max(answer,sm)

print(answer)
