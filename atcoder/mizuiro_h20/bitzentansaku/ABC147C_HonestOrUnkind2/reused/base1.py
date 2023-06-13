N = int(input())
L = [[] for i in range(N)]
for i in range(N):
    A = int(input())
    for _ in range(A):
        x,y = map(int, input().split())
        L[i].append([x-1,y])

ans = 0
for i in range(2 ** N):
    T = []#1からNについて正直者か(0→正直でない、1→正直)
    cnt = 0#使用する証言の個数
    for j in range(N):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            T.append(1)
            cnt+=1
        else:
            T.append(0)
    #矛盾しないかチェック
    f = True
    for j in range(N):
        if T[j]==1:#正直者の内容が正しいかどうか
            for x,y in L[j]:
                if T[x]!=y:
                    f = False
    if f:
        ans = max(ans,cnt)
print(ans)
