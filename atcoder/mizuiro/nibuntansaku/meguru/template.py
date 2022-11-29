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


# def solver():
#     result = 0
#     target = LI()
#     have = II()

#     # algorithm
#     return result

def upper_bound(t_list,ball):
    ng = -1
    ok = len(t_list)
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if(ball < t_list[mid]): # 値がまだ手元の情報の上→okを下げる
            ok = mid
        else: # 値がまだ手元の情報の下(手元情報と同じでも)→ngを上昇
            ng = mid
    return ok


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

if __name__ == "__main__":
    target = LI()
    have = II()
    sorted(target)
    print(target)
    print(have)
    answer1 = lower_bound(target, have)
    print("lower_bound -> {} : expect 2".format(answer1))
    answer2 = upper_bound(target, have)
    print("lower_bound -> {} : expect 5".format(answer2))
    # print("{}".format(solver()))
