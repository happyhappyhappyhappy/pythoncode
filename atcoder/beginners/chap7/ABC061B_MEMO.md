* 1回目
* 単純にfromList,toListを作ってappendで追加する
* [完了](https://atcoder.jp/contests/abc061/submissions/13765242)
    * ソースコードが若干長くなったぐらい。依然と同じ。
* 2回目
* 返し値を強引に1行にしてみるテスト
* よく考えればわざわざ引数を出る→入るにしないで一括にしても良いんじゃ無いか
* 最初にそれをやったらエラー発生→joinは文字列しか結合しないのにint型だったため
* 調べてみたら内包表記`[ str(j) for j in list]`で良い
    * [情報](https://note.nkmk.me/python-list-str-num-conversion/)
* 折角作ったのでこのまま返り値にする
* [完了](https://atcoder.jp/contests/abc061/submissions/14064087)
    * 1回目と同じ