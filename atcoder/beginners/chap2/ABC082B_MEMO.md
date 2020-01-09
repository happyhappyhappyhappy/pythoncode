# ABC082B-Two Anagrams

[Problem](https://atcoder.jp/contests/abc082/tasks/abc082_b)

---
## 1回目
# 2019/12/22

* 武器
  * [sort](https://note.nkmk.me/python-list-sort-sorted/)
  * [文字列比較](https://note.nkmk.me/python-str-compare/)
  * [逆にする](https://note.nkmk.me/python-reverse-reversed/)
* ネタが尽きたので答えを見る
  * [参考](https://atcoder.jp/contests/abc082/submissions/1929956)
* 疲れた
# 2019/12/25
* 再度武器を確認。「sort」「逆にする」を利用。答えは使わず
  * 文字列を`list`型に変換しないと`sorted`は使えず、`sorted`はまたイテレータ型になるので`reversed`するためには`list`にして`join`する必要がある。→本当か
* [完了](https://atcoder.jp/contests/abc082/submissions/9127423)
  * 実行時間は17msと他と同じ、メモリは一部3040kbになる以外他と同じ
---
## 2回目
# 2019/12/27
* 前の武器をそのまま使おうと思ったがTの入れ替えで最も辞書順が大きい所にSが届けなければ良いような気がする
  * つまりは、sortedを使うのはTだけということで
  * [失敗](https://atcoder.jp/contests/abc082/submissions/9158934)
    * `1_05.txt`,`1_07.txt`に穴があるっぽい
* 結局は1回目と同じ方法へする
  * [完成](https://atcoder.jp/contests/abc082/submissions/9158984)
* ちょっと物足りないので短縮版を載せてみる
  * [これ](https://atcoder.jp/contests/abc082/submissions/4345435)
    * `s=sorted`てもう関数をオブジェクトとして扱っていることか
    * あと実は`sorted`で直接文字列ソート(つまりはchar型iterater)として処理しているのか。
    * 次回要検証
---
## 3回目
### 2020/01/09
* 三項演算子の使い方[情報源](https://qiita.com/howmuch515/items/bf6d21f603d9736fb4a5)
    * `(変数) = (条件がTrueのときの値) if (条件) else (条件がFalseのときの値)`
* [sorted例](http://bit.ly/36ytxb8)
    * いずれも`join`が必要
* [完了](https://atcoder.jp/contests/abc082/submissions/9368114)
    *  `1_08.txt`のみ3060kbになるくらい