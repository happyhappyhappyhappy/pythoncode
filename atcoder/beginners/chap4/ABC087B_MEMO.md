# ABC087B-Coins

[Problem](https://atcoder.jp/contests/abc087/tasks/abc087_b)
-----
## 1回目
# 2020/03/13
* `sys.stdin.readlines()`はデータ終了が読み取れないため使いようが無さそう
    * 使うのであれば検証しよう
    * `readline()`は過去に検証したが動作に差は無い
* [完了](https://atcoder.jp/contests/abc087/submissions/10797639)
    * 実行時間高いと46ms,メモリは3060k
        * 依然とあまり替わらないかも
-----
## 2回目
# 2020/3/18
* 全然for文の結果が同じ値になっておかしいと思ったら、関数引数を足していたことが判明
* [完了](https://atcoder.jp/contests/abc087/submissions/10983825)
    * 時間、メモリなどは同じ
-----
## 3回目
# 2020/3/22
* atcoder用のスニペットと作ってみてやってみる
* print文の中はf文字列がフォーマットというが、これは3.6以降なので、atcoderに引っかかる可能性あり。使わない。
* また関数引数に引っかかった
* [完了](https://atcoder.jp/contests/abc087/submissions/11071223)
    * 時間メモリなどは同じ。