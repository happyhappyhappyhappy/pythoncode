# ABC042B-文字列大好きいろはちゃんイージー
[Problem](https://atcoder.jp/contests/abc042/tasks/abc042_b)
-----
# 1回目
## 2020/04/26
* 単純にくっつけて置く→ソートするのはダメかね
    * pythonは文字列→文字配列と見てしまえば通用しないか
    * 要検証
        * 問題なし
## 2020/4/27
* 後はjoinするくらい
* 問題発生→joinが上手くいかない
## 2020/4/28
* 原因はsplit関数はlist型を入れるので、データに出来るのはその1番目の値だけ
* [完了](https://atcoder.jp/contests/abc042/submissions/12452936)
    * 以前にやったよりはメモリも実行時間も少なめ
        * 時計を動かした後がある
-----
# 2回目
## 2020/4/29

* `tmpList , _ = map(str, sys.stdin.readline().split())`でサクッと行きたかったがエラー
* LSというLIを改良した関数を作成する
* [完了](https://atcoder.jp/contests/abc042/submissions/12474025)
-----
# 3回目
## 2020/5/3
* Stringクラスのjoinメソッドは元のStringをセパレーター、間に挟む文字なのでfor文に意味は無い
* [完了](https://atcoder.jp/contests/abc042/submissions/12700935)