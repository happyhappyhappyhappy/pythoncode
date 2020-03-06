# ABC053B-A to Z String

[Problem](https://atcoder.jp/contests/abc053/tasks/abc053_b)

---
## 1回目
# 2020/03/01
* 文字列はイテレータなので右から、左から検索して要素の位置を返すモジュールがあるが、今回は使わない物とする
* あまり変わらないかもしれないが問題の文字列オブジェクトをそのまま使わずコピーをして、そちらを利用して起動することにした。[参考](https://docs.python.org/ja/3/library/copy.html)
* [完了](https://atcoder.jp/contests/abc053/submissions/10423791)
    * 長くて36ms,メモリ大きくて4012kb
---
## 2回目
# 2020/03/06
* 今回は開発スピード重視のため前回と同じアルゴリズムにした
* classを使うのは当分やめた。テーマが進まない。
* [完了](https://atcoder.jp/contests/abc053/submissions/10564276)
    * 処理時間は06.txtのみ29ms,メモリ利用は最大3516kb
    * クラスを使うとメモリは多くなるのか