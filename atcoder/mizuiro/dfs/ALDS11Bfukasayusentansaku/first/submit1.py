import sys
input2 = sys.stdin.readline
from collections import deque
import pprint as pp
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


# Const
MAXSIZE = ( 1 << 31 ) -1
MINSIZE = -( 1 << 31) + 1


def solver(N):
    result = [[[-1]*(N+1)]*(N+1)]
    G=[deque([]) for _ in range(N+1)] # グラフ本体
    # 情報収集
    u,k,*v = [int(x) for x in input2().split()]
    v.sort()
    for j in v:
        G[u].append(j)
    time=0
    arrival_time=[-1]*(N+1)
    finish_time =[-1]*(N+1)
    # やはり使いこなせない。別途呼び出し

    # 初期化
    return result


if __name__ == "__main__":
    N = int(input2())
    x=solver(N)
    print("{}".format(x))
