import sys
input2 = sys.stdin.readline
from collections import deque

d = deque('ghi')
for elem in d:
    print(elem.upper())
d.append('j')
d.appendleft('x')
for elem in d:
    print(elem.upper())

# https://docs.python.org/ja/3.10/library/collections.html?highlight=deque#collections.deque
