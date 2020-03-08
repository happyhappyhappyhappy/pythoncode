# ABC095B-Bitter Alchemy
[Problem](https://atcoder.jp/contests/abc095/tasks/abc095_b)
-----
## 1回目
# 2020/03/07
* まずは入力データは一行目は`input()`使って、二つの変数にする
* それ以降は`readlines`の手法が使えそうだが、まず一回目は様子見でNの数だけ回して、次々listにappendする[参考](https://qiita.com/rsakamot/items/2277e26e3716e8f8f5a2#append)
* [完了](https://atcoder.jp/contests/abc095/submissions/10585886)
    * 実行時間は全部17ms,メモリは一部3064kb
* 割り算の演算子は`/ と // ` 前者は小数まで出す。後者は切り捨て整数。[ソース元確認](http://www.tohoho-web.com/python/operators.html)、本家は気が向いたら探す。

## 2回目
# 2020/03/08
* 1行目は同じ、2行目以降はreadlinesを使う
    * 1回だけまずは使って表示させてみよう
        * パス、上手くいかない→やっぱりなんでこれを使おうと考えたかしらべよう
* 全部の必要量の合計はsum関数を使い、最小の量はmin関数を使う
    * [参考文献](https://docs.python.org/ja/3/library/functions.html)
* こまめにAtokの全角半角チェックをしよう
* [完了](https://atcoder.jp/contests/abc095/submissions/10666393)
    * 単純化出来たのは良かったかも
    * 機械的な情報は前回と同じかな