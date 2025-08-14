import sys
from collections import Counter

def solver():
    # 入力処理は変わらないよ！
    _, m = map(int, sys.stdin.readline().split())

    # リストAの要素の出現回数を数える
    # このCounterがマジで便利！{"要素": 個数}みたいな辞書形式で持てるの！
    a_counter = Counter(map(int, sys.stdin.readline().split()))

    # リストBの要素を受け取る
    b_list = list(map(int, sys.stdin.readline().split()))

    # Bの各要素について、AのCounterから1つずつ減らす
    for b_item in b_list:
        # 要素がa_counterに存在し、かつその個数が1以上だったら
        if a_counter.get(b_item, 0) > 0:
            a_counter[b_item] -= 1
            
    # 削除した後の残りの要素をリストに変換して返す！
    # a_counter.elements()で元の要素のリストが再構築できるんだ！天才すぎない！？
    return list(a_counter.elements())

if __name__ == "__main__":
    result = solver()
    print(*result)