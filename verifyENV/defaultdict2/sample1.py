# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
from collections import defaultdict
# pypy3用
# import pypyjit
# 再帰制御解放
# pypyjit.set_param('max_unroll_recursion=-1')
# sys.setrecursionlimit(10**6)
from logging import getLogger, StreamHandler, DEBUG

# 入力のマクロ
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

# デバッグ出力の作成
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

# クラス+メソッドを一関数
xdebug=logger.debug
ppp=pp.pprint
# Const
MAXSIZE = ( 1 << 59 ) -1
MINSIZE = -( 1 << 59) + 1

d = defaultdict(list)
s = []
s.append(('yellow',1))
s.append(('blue',2))
s.append(('yellow',3))
s.append(('blue',4))
s.append(('red',3))
s.append(('yellow','banana'))
print(f"s={s}")
print(f"d={d}")
for colors,num in s:
    d[colors].append(num)
print(f"d={d}")
for c,n in d.items():
    print(f"{c}->{n}")
for val in d.values():
    print(f"val->{val}")
for key in d.keys():
	print(f"key->{key}")
