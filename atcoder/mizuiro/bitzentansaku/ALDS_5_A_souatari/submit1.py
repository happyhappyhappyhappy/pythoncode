import sys
# from collections import defaultdict
# import heapq,copy
input2 = sys.stdin.readline
import pprint as pp
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


# Const
MAXSIZE = ( 1 << 31 ) -1
MINSIZE = -( 1 << 31) + 1


def rec(pos,all_pos,balance,g_List):
    if balance == 0:
        return True
    if pos == all_pos :
        return False
    if balance < 0 :
        return False
    # 最終位置までは行かず、まだbalanceが余った物について一つ値を進める
    return rec(pos+1,all_pos,balance-g_List[pos],g_List) or rec(pos+1,all_pos,balance,g_List)

def solver(gList,i_sum):
    result = rec(0,len(gList),i_sum,gList)
    # algorithm

    return result


if __name__ == "__main__":
    givenNum = II()
    noList = [ int(x) for x in (input2().split())]
    solveNum = II()
    solveList = [ int(x) for x in (input2().split())]
    for x in range(solveNum):
        if solver(noList,solveList[x]):
            print("yes")
        else:
            print("no")
