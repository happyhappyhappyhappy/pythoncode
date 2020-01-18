# ABC081B-Shift only

[Problem](https://atcoder.jp/contests/abc081/tasks/abc081_b)

---
## 1回目

# 2020/01/10
* おすすめであるという`readline`入力でトライ
* 入力時に`list(map(int,readline()))`にして配列に入れる必要がある
    * これをしないと少なくとも改行は入れられてしまうので注意
# 2020/01/13
* 整数の最大値は`sys.sys.maxsize`。[情報源](https://docs.python.org/ja/3/library/sys.html#sys.maxsize)
* なかなかすすまない

# 2020/01/17
* 基本的なfor->if文で引っかかる。忘れたのか。

# 2020/01/18
* 時間ができた
* ifの問題は基本的にpythonはindentが括弧の指定をするので括弧は余計だった
* [完了](https://atcoder.jp/contests/abc081/submissions/9557668)
    * 時間は19ms,メモリは3040kbなので`sys.readline`にするメリットはなし

