# ABC068B-Break Number

[Problem](https://atcoder.jp/contests/abc068/tasks/abc068_b)

---
## 1回目

# 2020/01/19
* 無難に割れるカウンター配列を作成→この配列の最大値を求める流れで
    * 多分配列作成時にまとめてできるような気はするが
* [完了](https://atcoder.jp/contests/abc068/submissions/9595690)
    * 他の問題と実行時間・メモリ量は変わらないがもう少し速く・小さくならんかねぇ

## 2回目
# 2020/01/23
* カウンター配列を省略しようとしたがいきなりコードはきつかった
    * 実行したら全部WA
* 今回も諦める
* yapf,VSCode上で実行できる方法ないものかねぇ
    * 「コマンドパレット」＞「フォーマットする」で出来た気がする
# 2020/01/24
* pylintは諦めるか、`~/.config/pylintrc`で省略されているか落ち着いたら確認
* [完了](https://atcoder.jp/contests/abc068/submissions/9698082)
    * 他の問題と実行時間、メモリ量は変わらず
## 3回目
# 2020/01/25
* 今回も前回までの同じ情報で行く
    * 取りやめ。やはりしらべながら行く
        * 2で何回割れるかを調べる関数を作ってみる
    * 入力に`N = list(map(int, sys.stdin))`を使っているのだが何故かインプットが終わらないため調査したい
    * 原因は`readline().rsplit()`を使わなかったため
        * `readline`は一行読み込む,`rsplit`は改行を取り除くため
        * これでlist型になる
* [完了](https://atcoder.jp/contests/abc068/submissions/9838607)
    * 実行時間17or18ms,メモリ2940kb,3060kb
        * 入力数が大きくなれば変わるかしら
