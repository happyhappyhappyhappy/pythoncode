import sys
import heapq

def solver():
    """
    クエリを処理して、最小値を取り出す操作の結果を返す関数。
    """
    
    # 処理するクエリの数を取得
    num_queries = int(sys.stdin.readline())

    # 最小値の取り出しが効率的なヒープを使うよ！
    min_heap = []
    
    # 結果を保存するリスト
    results = []

    # クエリの数だけループして処理
    for _ in range(num_queries):
        query = sys.stdin.readline().split()
        
        # クエリのタイプをチェック
        query_type = query[0]
        
        # '1'の場合はヒープに値を追加
        if query_type == '1':
            value_to_add = int(query[1])
            # heapq.heappushでヒープに要素を追加するよ
            heapq.heappush(min_heap, value_to_add)
            
        # '2'の場合はヒープから最小値を取り出して結果に保存
        elif query_type == '2':
            # heapq.heappopでヒープから最小値を取り出すよ
            min_value = heapq.heappop(min_heap)
            results.append(min_value)
            
    return results

# ここから実行！
if __name__ == "__main__":
    output_results = solver()
    for result in output_results:
        print(result)