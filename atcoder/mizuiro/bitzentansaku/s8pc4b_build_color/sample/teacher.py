n, k = map(int, input().split())
a = list(map(int, input(). split()))

res = 1 << 60 # 最小値が知りたいので答えの初期値はでかい数で
for i in range(1<<n): # k 個のビルが条件を満たすとし、その選び方をbit全探索する。選んだビル数がk以外の時はcontinueという方法で
    if(i%2 == 0): continue # 先頭のビルを見ないのは不可能なので一つ目のbitは必ず立っている必要がありその必要十分条件は「奇数であること」（最初のbitが1）

    use_idx = [0 for _ in range(n)] # どのビルに着目するか 0: 無視
    use_cnt = 0 # 着目するビルの数 kになる時だけ考える
    for j in range(n):
        if(i & (1<<j)):
            use_idx[j] = 1 # 1: 着目
            use_cnt += 1 # ＋＋着目

    if(use_cnt != k): continue # k個のビルに着目することだけを考える

    sm = 0 # 一つ目、先頭。いじる必要はないのでコストも0
    mx = a[0] # 先頭の高さが暫定最大の高さ
    for j in range(1, n):

        if(use_idx[j]): # 二つ目からみていく
            if(a[j] <= mx): # もし暫定最大の高さがこのビル以上の高さならば
                sm += mx+1 - a[j] # このビルは最大＋１の高さまで最低伸ばす必要があり
                mx += 1 # その高さが暫定最大の高さになる

        mx = max(mx, a[j]) # 着目するビルかどうかにかかわらず暫定最大高さは更新される（これをif(use)内に書くとだめだよ。見ないからと言って透明にはならないので）

    res = min(res, sm) # 全てのコストを計算したら暫定最安コストと戦う

print(res)
