# ARC090B-Palindromic Numbers
[Problem](https://atcoder.jp/contests/abc090/tasks/abc090_b)
-----
## 1回目
# 2020/4/12
* 基本的には文字列を与えて逆順にして全部同じであれば良いか
* [配列のスライス化で反転させる](https://note.nkmk.me/python-reverse-reversed/)
* 中身が同じか組み込み関数でチェックできるかと思ったが面倒くさそうなので無難にfor文で回す
* [完了](https://atcoder.jp/contests/abc090/submissions/3882093)
    * 一度やったより実行時間が長いのは幅の大きな時の時間の感じ
        * 前回は0,1だけ使っていた
-----
## 2回目
# 2020/4/13
* 短縮検索法で行く
    * 1番目と2番目だけ
* そういえばわざわざ文字列を逆転させる必要無かった
* [完了](https://atcoder.jp/contests/abc090/submissions/11889395)
    * 処理も速くなった
-----
## 3回目
# 2020/4/15
* チェック用の別関数を用意する
* while文を用いる
* 時間が無いので実行はしない