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