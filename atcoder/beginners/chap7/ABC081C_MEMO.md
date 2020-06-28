* 1回目実行メモ
    * collectionライブラリを入れてくる
    * pprintライブラリを導入し、`prp = pprint.pprint`とする
        * ただ印字させたいだけならばこれを使うと後で、pprintをコメントすればこれに引きずられてまとめてエラーが出る
    * dict型のソートには`key=lambda x:x[1]`を付けておくこと
    * [完了](https://atcoder.jp/contests/abc081/submissions/14805278)
        * collectionライブラリの導入でメモリは多めになってしまった