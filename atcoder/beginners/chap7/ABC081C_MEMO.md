* 1回目実行メモ
    * collectionライブラリを入れてくる
    * pprintライブラリを導入し、`prp = pprint.pprint`とする
        * ただ印字させたいだけならばこれを使うと後で、pprintをコメントすればこれに引きずられてまとめてエラーが出る
    * dict型のソートには`key=lambda x:x[1]`を付けておくこと
    * [完了](https://atcoder.jp/contests/abc081/submissions/14805278)
        * collectionライブラリの導入でメモリは多めになってしまった
* 2回目実行メモ
    * ライブラリからCounterクラスを呼び出す
    * 辞書型のクラスには値だけ抜き出すvalues()メソッドがあるのでこれとlistの抱き合わせで楽にする
    * [完了](https://atcoder.jp/contests/abc081/submissions/14863948)
        * Counterだけ呼び出したためメモリは減少した
* 3回目実行メモ
    * 2回目とほぼ同じ構造になった従って結果もほぼ同じ
    * 途中で与えられた値同士で引き算してはまった。何が与えられているかよく読もう
    * [完了](https://atcoder.jp/contests/abc081/submissions/14863948)
        * 2回目と同様