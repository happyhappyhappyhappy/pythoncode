# ABC102B-Maximum Difference

[Problem](https://atcoder.jp/contests/abc102/tasks/abc102_b)

---
## 1回目

# 2020/01/24
* まずソートをかけてしまって、`最後の数-最初の数`を出してしまうか
# 2020/01/25
* やはり今後のことを考えて`sys.stdin.readlnes()`で取り出す
* [完了](https://atcoder.jp/contests/abc102/submissions/9712626)
    * 実行時間やメモリは他と変わらない次は「N^2」覚悟の上全組み合わせを調べてみるか100個しかないし
---
## 2回目
# 2020/02/01
* 全検索作戦
* [完了](https://atcoder.jp/contests/abc102/submissions/9866039)
    * 最終的に実行時間は19ms(+2ms),メモリ3184(+200k)程度

---
## 3回目
# 2020/02/08
* 1回目と同じ戦略
    * `list.sorted()`は値を返す、 `list.sort()`はlistを壊して(整列して)値は返さない点違うところ→今回は値を直接変える`sort`を利用
        * 後、オプションはヒントでは`reverse`を表示してくれるが、結局は`reversed`と受け身のオプションしかないので自動生成に注意
* [完了](https://atcoder.jp/contests/abc102/submissions/9953187)
    * 利用メモリは減っている
    * 今回よりpylintの利用に従う余り変数名を短縮にしてしまった