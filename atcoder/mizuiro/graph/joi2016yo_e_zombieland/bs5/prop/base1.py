import queue

# FIFOキュー（先入れ先出し）
fifo_queue = queue.Queue()

# キューに要素を追加
fifo_queue.put(1)
fifo_queue.put(2)
fifo_queue.put(3)

# キューから要素を取り出す
item1 = fifo_queue.get()
item2 = fifo_queue.get()
item3 = fifo_queue.get()

print("FIFO Queue:")
print(item1)
print(item2)
print(item3)

# LIFOキュー（後入れ先出し）
lifo_queue = queue.LifoQueue()

# キューに要素を追加
lifo_queue.put(1)
lifo_queue.put(2)
lifo_queue.put(3)

# キューから要素を取り出す
item1 = lifo_queue.get()
item2 = lifo_queue.get()
item3 = lifo_queue.get()

print("\nLIFO Queue:")
print(item1)
print(item2)
print(item3)

# 優先度付きキュー（要素に優先度を付けて取り出す）
priority_queue = queue.PriorityQueue()

# キューに要素を追加（(優先度, 要素) のタプルで指定）
priority_queue.put((3, "apple"))
priority_queue.put((1, "banana"))
priority_queue.put((2, "cherry"))

# キューから要素を取り出す
item1 = priority_queue.get()
item2 = priority_queue.get()
item3 = priority_queue.get()

print("\nPriority Queue:")
print(item1)
print(item2)
print(item3)
