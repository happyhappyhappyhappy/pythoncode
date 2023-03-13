# stackとしてのdequeの使い方を覚える
from collections import deque
x = [1,2,3,4,5]
my_queue=deque(x)
y = my_queue.pop()
print(y)
my_queue.append(7)
y=my_queue.pop()
print(y)
