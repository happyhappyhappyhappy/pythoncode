# ABC113B-Palace

[Problem](https://atcoder.jp/contests/abc113/tasks/abc113_b)

---
## 1回目

# 2020/02/06
* [完了](https://atcoder.jp/contests/abc113/submissions/9926085)
    * ようやく本格的かメモリが3060kbになる。実行時間は同じ。

* `sys.stdin.readline().rsplit()`使っているのだが効果無し
* 1-indexで最終値を求めている様なので、pythonの配列は0-indexを考えて初期値は0にして返り値を+1して返した
* `print"{} {}".format(a, b)`の形式を多用した。忘れないようにすぐに使おう。
---
## 2回目
* 最終的に比較する値は分解してしまえばもっと単純な値同士の比較になると思った
    * これは3回目に取っておく=>失敗。最大と最小の間にAが来られてはたまらない
* 3項演算子利用。まだ覚えられない。[参考](https://qiita.com/howmuch515/items/bf6d21f603d9736fb4a5)
    * 二つの値を更新するのでこれは意味が無い
* 累乗は公式ドキュメントでmathパッケージを入れなければいけない感じであった。
    * 冪乗で調べれば組み込み関数で'**'を使えば良かった
* [完了](https://atcoder.jp/contests/abc113/submissions/10088701)
    * 特に大きな差は無い
