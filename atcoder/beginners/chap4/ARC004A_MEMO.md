# ARC004A-2点間距離の最大値
[Problem](https://atcoder.jp/contests/arc004/tasks/arc004_1)
-----
## 1回目
# 2020/3/27
* 最初出力がおかしかったが原因を見れば二点の差を出すのが目的だった
    * 最初は(0,0)から全点を見ていた
    * 落ち着けば分かった
* [完了](https://atcoder.jp/contests/arc004/submissions/11229171)
    * python3は29ms,3572kbで完了のまき
-----
## 2回目
# 2020/3/28
* 2次元配列使って見る
* 確か無造作に宣言するとidが同じ故に一部の更新が全体の更新になることを考慮する
* [参考リンク](https://note.nkmk.me/python-list-initialize/)
    * 上手くいった
        * [復習](https://note.nkmk.me/python-list-comprehension/)
    * 内包表記だけできてしまったぽい(2020/3/29)
        * 誤った例`[ [0] * 2 ] * 3`
* 次はzipでやってみよう
    [参考リンク](https://note.nkmk.me/python-list-comprehension/)
* [完了](https://atcoder.jp/contests/arc004/submissions/11343213)
    * 実行時の長さは少し長くなった。メモリは同じ。
-----
## 3回目
# 2020/X/X
