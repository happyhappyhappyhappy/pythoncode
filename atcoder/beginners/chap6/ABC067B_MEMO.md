# ABC067B- Snake Toy
[Problem](https://atcoder.jp/contests/abc067/tasks/abc067_b)
-----
# 1回目
## 2020/04/21
* リストを逆順にソートして大きい順から数えれば良し。
* sortが分からなくなった
    * sortedは新たなオブジェクトを作成する
        * 元のオブジェクトは壊さない
    * 結局sortを利用
* while 使って見るか
* [完了](https://atcoder.jp/contests/abc067/submissions/12195296)
    * 実行時間は前より良いのか、その辺は不明。
        * 前のは色々インポートしていてややこしい
-----
# 2回目
## 2020/04/23
* sortedにreserveという引数は無い
    * reverseとvとsが逆
* [完了](https://atcoder.jp/contests/abc067/submissions/12269559)
    * 1回目と変わらない
-----
# 3回目
## 2020/4/29
* あえてsortedを使い元をそのままにする
* [完了](https://atcoder.jp/contests/abc067/submissions/12473127)