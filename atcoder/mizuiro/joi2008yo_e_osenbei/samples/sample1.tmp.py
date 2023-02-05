import os

r,c = list(map(int,input().split()))
senbe = []#1が黒 0が白　1を減らすのが目的。0の数を最大化。
for i in range(r):
    senbe.append(list(map(int,input().split())))
#print(r,c,senbe)
#rの上限 10 は c の上限 10000 に比べて小さいことに注意せよ。

#rのパターンを作る。
keta = "0"+str(r)+"b"
patterns = [format(i,keta) for i in range(2**r)]#スイッチの数分
patterns = [[int(ii) for ii in list(i)] for i in patterns]
#print(patterns)
#どちらでもいいが、0をその行を裏返さない、1をその行を裏返す、とする。

#res = [[]]*len(patterns)#これがだめ deepcopyじゃないと。
res = []
for i in patterns:
    res.append([])

#各列に対して、各パターンについて調べる。
#各パターンについて列が表か裏かで0の数が多い方を記録して各パターンに対応する配列に保持する。
#最後に各パターンの配列を各々合計して合計が小さいものを選ぶ。

for clm_i in range(c):#各列に対して 5
    tmp = 0
    for pattern_i in range(len(patterns)):#各行の状態パターン各々に対して 4
        tmp1 = tmp2 = 0
        for row_i in range(r):#各パターンの各行の結果を合計して配列に保持する。
            row_v = patterns[pattern_i][row_i]#その行を裏返す場合が1 裏返さないのが0
            #その列を裏返さない場合
            if senbe[row_i][clm_i] == 0 and row_v == 0:#せんべが表で裏返さない
                tmp1 += 0#そのまんま
            if senbe[row_i][clm_i] == 0 and row_v == 1:
                tmp1 += 1#1回裏返すので
            if senbe[row_i][clm_i] == 1 and row_v == 0:#せんべが表で裏返さない
                tmp1 += 1#1回裏返すの絵
            if senbe[row_i][clm_i] == 1 and row_v == 1:
                tmp1 += 0#2回裏返すので
            #その列を裏返す場合 上記と全て逆
            if senbe[row_i][clm_i] == 0 and row_v == 0:
                tmp2 += 1
            if senbe[row_i][clm_i] == 0 and row_v == 1:
                tmp2 += 0
            if senbe[row_i][clm_i] == 1 and row_v == 0:
                tmp2 += 0
            if senbe[row_i][clm_i] == 1 and row_v == 1:
                tmp2 += 1
        #print(tmp1,tmp2)
        tmp = min(tmp1,tmp2)#その列をうらがえすのとうらがえさないのでどちらかの結果を採用。0が多い方法を採用。
        res[pattern_i].append(tmp)#各行の状態パターン各々に対して、結果を加える。

#for i in res:
#    print(i)

print(r*c - min([sum(i) for i in res]))
