import bisect

N=int(input())
L_LIST=[]
H_LIST=[]
for _ in range(N):
    H,L=map(int,input().split(" "))
    H_LIST.append(H)
    L_LIST.append(L)
Q=int(input())
T=list(map(int,input().split(" ")))

max_list=[]
cur_max=0
for j in range(N-1,-1,-1):
    cur_max=max(cur_max,H_LIST[j])
    max_list.append(cur_max)
max_list.reverse()
print(max_list)
print(L_LIST)
for t in T:
    index=bisect.bisect_right(L_LIST,t)
    print(max_list[index])

