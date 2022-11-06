import sys
# from collections import defaultdict
# import heapq,copy
import pprint as pp
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def TI(): return tuple(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


# Const
MAXSIZE = ( 1 << 31 ) -1
MINSIZE = -( 1 << 31) + 1


def solver(figI,figL,realI,realL):
    moveDict = dict()
    for j in range(figI):
        for k in range(realI):
            (figx,figy) = figL[j]
            (realx,realy) = realL[k]
            diffx = realx-figx
            diffy = realy-figy
            print("x軸 {} へ移動+y軸 {} へ移動".format(diffx,diffy))
            difftuple = tuple(diffx,diffy)
            # TODO: ここから確認 C++と同じように行ければ良いのだが
            moveDict[difftuple] = moveDict[difftuple]+1

    result = 0
    # algorithm
    return result


if __name__ == "__main__":
    figureInt = II()
    figureList = []
    for j in range(figureInt):
        tuple1 = TI()
        figureList.append(tuple1)
    realInt = II()
    realList = []
    for j in range(realInt):
        tuple1 = TI()
        realList.append(tuple1)
    print("-----星座の図鑑一覧-----")
    for j in range(figureInt):
        print("{} => {}".format(j,figureList[j]))
    print("-----実際の空の一覧-----\n")
    for j in range(realInt):
        print("{} => {}".format(j,realList[j]))
    print("{}".format(solver(figureInt,figureList,realInt,realList)))
