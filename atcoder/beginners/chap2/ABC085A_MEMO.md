# ABC085A-Already 2018

[Problem](https://atcoder.jp/contests/abc085/tasks/abc085_a)

---
## 1回目
# 2019/12/20
* 文字列の抽出と結合は追って勉強
* [完了](https://atcoder.jp/contests/abc085/submissions/9038758)
  * メモリと実行時間は他と変わらず
---
## 2回目
* `"2018".join("/01/07")`としてみたが`/20180201812018/2018020187`になる
  * 結局[ここ](https://note.nkmk.me/python-string-concat/)で調べる
    * これは文字間に置き換える感じになる→意味が無い
  * `+`を使った方がベター
    * `''.join("2018","/01/07"`で行けば良かった→次回これで
    * `("2018" "/01/07")`でも出来る？
      * [これ](https://docs.python.org/ja/3/library/stdtypes.html#textseq)参照
* [完了](https://atcoder.jp/contests/abc085/submissions/9047503)
  * ほぼ同じ感じ
---
## 3回目
* `list`に直して置換して、再結合
  * 面倒くさいがコピーして4文字目だけを8にする
  * `for`文で`result`に放り込む→中止
  * [ここ](https://qiita.com/utgwkk/items/5ad2527f19150ae33322)を見て似たようなケース発見
    * `copy`モジュールをインポートした上で、`deepcopy`し、4番目の値を変えれば出来る
    * 後は全部`join`で空白無しで結合する
* 何故か`solver`関数のオブジェクト型が出力されたが、それは単に`print(solver())`とミスったせい
* [完了](https://atcoder.jp/contests/abc085/submissions/9143571)
  * 各種データは22ms、3444KBと若干数値が上がる。練習としては丁度良かったか

