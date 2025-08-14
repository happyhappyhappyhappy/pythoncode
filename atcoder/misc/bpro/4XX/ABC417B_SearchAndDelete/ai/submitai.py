import sys

def solver():
    # 入力処理: NとMは使ってないから、アンスコ(_)にするのが賢いかな！
    _, m = map(int, sys.stdin.readline().split())
    # 集合（set）を使うと、要素の存在チェックがめっちゃ速くなるよ！
    # 探索のたびにリスト全体を舐めるのは効率が悪いからね！
    a_set = set(map(int, sys.stdin.readline().split()))
    # Bの要素をリストで受け取る
    b_list = list(map(int, sys.stdin.readline().split()))

    # Bの各要素について、Aの集合から削除する
    for b_item in b_list:
        # 要素が集合に存在すれば削除
        if b_item in a_set:
            a_set.remove(b_item)
    # 結果をソートしてリストに変換して返す！
    return sorted(list(a_set))

if __name__ == "__main__":
    result = solver()
    print(*result)
