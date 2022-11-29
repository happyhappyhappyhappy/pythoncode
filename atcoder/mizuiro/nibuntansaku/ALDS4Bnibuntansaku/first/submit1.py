import sys
# from collections import defaultdict
# import heapq,copy
import pprint as pp
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


# Const
MAXSIZE = ( 1 << 31 ) -1
MINSIZE = -( 1 << 31) + 1

def lower_bound(t_list,ball):
    ng = -1
    ok = len(t_list)
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if(ball <= t_list[mid]): # 値がまだ手元の情報の上→okを下げる
            ok = mid
        else: # 値がまだ手元の情報の下→ngを上昇
            ng = mid
    return ok

def solver(s_size,S,t_size,T):
    result = 0
    # algorithm
    for j in range(0,t_size):
        x = lower_bound(S, T[j])
        if s_size <= x or s_size < 0:
            continue
        if S[x] == T[j]:
            result = result + 1
    return result


if __name__ == "__main__":
    n = II()
    S = LI()
    q = II()
    T = LI()
    print("{}".format(solver(n,S,q,T)))
