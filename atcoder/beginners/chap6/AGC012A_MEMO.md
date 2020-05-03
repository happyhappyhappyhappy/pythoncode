(テンプレート)
# AGC027A-Candy Distribution Again
[Problem](https://atcoder.jp/contests/agc027/tasks/agc027_a)
-----
# 1回目
## 2020/04/29
* きっかりで与えなければいけない
    * 足りなくてももらいすぎでもダメ
        * ちょっとまず解説を見てみるか
    * 不要。もらいたい数の合計 < 持っている個数なら最後の一人は不満足なだけ
        * 後は順に与えていれば良し
* 実装は次の日
## 2020/4/30
* 方向転換
    * 全員に配るループを回して途中でお菓子がマイナスになったらその場で抜ける
        * 最後まで配りきってなおかつ余っていれば一人減らす
* [完了](https://atcoder.jp/contests/agc027/submissions/12514913)
    * 一発だった
-----
# 2回目
## 2020/05/03
* [完了](https://atcoder.jp/contests/agc027/submissions/12702340)
