# ライブラリのインポート
# import heapq,copy
import pprint as pp
import sys

# from collections import deque
# pypy3用
# import pypyjit
# 再帰制御解放
# pypyjit.set_param('max_unroll_recursion=-1')
# sys.setrecursionlimit(10**6)
from logging import DEBUG, StreamHandler, getLogger

# 入力のマクロ
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number:int): return [LI() for _ in range(rows_number)]

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

def diff(s_char,t_char):
    res=0
    s_int=ord(s_char)-ord("0")
    t_int=ord(t_char)-ord("0")
    if s_int < t_int:
        res=s_int+10-t_int
    else:
        res=s_int-t_int
    return res

def solver():
    res = MAXSIZE
    N,M=MI()
    S=input()
    T=input()
    for j in range(N-M+1):
        now_res=0
        for k in range(M):
            now_res+=diff(S[j+k],T[k])
        res=min(now_res,res)
    return res

if __name__ == "__main__":
    res=solver()
    print(res)

