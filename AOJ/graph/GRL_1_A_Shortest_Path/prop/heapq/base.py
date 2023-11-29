import heapq

# ヒープに要素を追加
heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
heapq.heappush(heap, 9)

print("Heap after insertion:", heap)

# 最小の要素を取り出す
min_element = heapq.heappop(heap)
print("Min element:", min_element)
print("Heap after popping the minimum element:", heap)

# 最小の要素を取り出さずに確認する
min_element = heap[0]
print("Min element without popping:", min_element)

# ヒープソートの例
sorted_elements = []
while heap:
    sorted_elements.append(heapq.heappop(heap))

print("Sorted elements using heap sort:", sorted_elements)
