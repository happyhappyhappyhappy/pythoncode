import sys
input2 = sys.stdin.readline
from collections import deque

# この*vがどのような動作をしているかテストしたいだけ
u,k,*v = input2().split()
print("u = {}".format(u))
print("k = {}".format(k))
print("v = {}".format(v))
print("v の 要素は {} 個".format(len(v)))
