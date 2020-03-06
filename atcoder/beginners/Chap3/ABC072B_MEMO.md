# ABC072B-OddString

[Problem](https://atcoder.jp/contests/abc072/tasks/abc072_b)

---
## 1回目
# 2020/02/14
* とりあえず形整えただけで終わり
* [完了](https://atcoder.jp/contests/abc072/submissions/10125618)
    * 処理時間は23ms,メモリは長いと3542kb
* answer変数はリストにして、最後にanswer[0]で返すか
---
## 2回目
# 2020/02/27
* 間が空いた
* ABC113Bと同じくクラスを使って行う
* Using EditorConfig core...{}が気になる
* 3項演算子の利用はせず
* [完了](https://atcoder.jp/contests/abc072/submissions/me)
    * 処理時間は30ms,メモリは変わらず
---
## 3回目
# 2020/03/07
* また間が空いた
* 今度は`class`のメソッド関数に`__str__`を試しに使って見た
* とりあえずtestdataの確認に使ったが上手くいった
    * object を直接していたい時だけ`print(object)`で表示する文字列を求める
* [完了](https://atcoder.jp/contests/abc072/submissions/10557434)
    * 実行時間は22ms,メモリは3044kbと若干増えた

* 次回以降、この課題をやる目的はアルゴリズムの習得なので、直接の解法は外部関数にするがクラスの設定はしない
    * デバッグで使える物としよう

* なお、今回の`__str__`関連は[ここ](https://note.nkmk.me/python-union-find/)を参照
* `while` 文ははまり防止の為一応、print文をまずはめておきたい
* `copy.copy(オブジェクト)`ね
