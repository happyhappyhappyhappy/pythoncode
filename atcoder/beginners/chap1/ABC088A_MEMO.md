# ABC088A-Infinite Coins

[Problem](https://atcoder.jp/contests/abc088/tasks/abc088_a)

---
## 1回目

# 2019/12/01
* メインコードの書き方は？
    * [ここ](https://blog.pyq.jp/entry/Python_kaiketsu_180207)参照
    * `if __name__ == "__main__":`の様だ
# 2019/12/06
* pylintが関数の最後のスペースを削除していないと怒られるので`settings.json`で次のことを設定
    * `"files.trimTrailingWhitespace": true`
    * [参考はこちら](https://qiita.com/iwata-n/items/39dc0e4391277589878b)
* [完了](https://atcoder.jp/contests/abc088/submissions/8809591)
    * 他の問題と実行時間とメモリは同じ
---
## 2回目
# 2019/12/08
* 関数を使って単純化を図る
* [完了](https://atcoder.jp/contests/abc088/submissions/8834221)
    * 実行時間は+1ms,メモリは同じ
---
## 3回目
# 2019/12/12
* 2回目と同じ戦略
* [失敗](https://atcoder.jp/contests/abc088/submissions/8922955)
* [成功](https://atcoder.jp/contests/abc088/submissions/8922990)
    * 間違えた原因は前者は500円を`//`(商)、後者は`%`(余り)にしたため。
    単純な設定のはずだが
    * 実行時間とメモリは前回と同じ。