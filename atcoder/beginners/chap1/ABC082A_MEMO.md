# ABC082A-Round Up the Mean

[Problem](https://atcoder.jp/contests/abc082/tasks/abc082_a)

---
## 1回目

# 2019/12/08
* いきなり関数化
* [完了](https://atcoder.jp/contests/abc082/submissions/8834690)
    * 実行時間が全部17ms。遅くなるのか。
    * メモリは同じ量
---
## 2回目
# 2019/12/13
* 色んなフォルダや問題ではまりまくってた
* [失敗](https://atcoder.jp/contests/abc082/submissions/8935043)
    * 原因は予想通り`X.5`になると`X`になってしまう
        * テストすらエラーになってしまうのを初めて知った
* [完了](https://atcoder.jp/contests/abc082/submissions/8935143)
    * メモリと実行時間は前と同じ
* 次回は`ceil`を使って見る。情報先は[こちら](https://docs.python.org/ja/3.8/library/math.html?highlight=ceil#math.ceil)
    * 小数点で返すかもしれないかどうか不安なので一旦出力させる
    * テストは必ず通す物とする
    * 後、mathライブラリを使うのでどうやってインポートするか
---
## 3回目
# 2019/12/XX