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


def dfs(pos,all_pos,balance,g_List):
    print("現在の位置 : {}   全部の数 : {}".format(pos,all_pos))
    print("余りの値 : {}".format(balance))
    print("与えられたリスト : {}".format(g_List))
    if balance == 0:
        print("めでたくぴったりの値になった")
        return True
    if balance < 0 :
        # TODO: ここの出力部分を書くところからスタート
        return False
    if pos == all_pos :
        print("")
        return False


    return dfs(pos+1,all_pos,balance-g_List[pos],g_List) or dfs(pos+1,all_pos,balance,g_List)

def solver(gList,i_sum):
    print("List {} から {} が出来るか確認する".format(gList,i_sum))
    result = dfs(0,len(gList),i_sum,gList)
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
