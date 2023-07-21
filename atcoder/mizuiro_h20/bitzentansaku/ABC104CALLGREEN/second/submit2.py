# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pprint
# from collections import deque
# pypy3用
import pypyjit
# 再帰制御解放
pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)
from logging import getLogger, StreamHandler, DEBUG

# 入力のマクロ
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


# Const
MAXSIZE = ( 1 << 59 ) -1
MINSIZE = -( 1 << 59) + 1


# データ取得
D,G=MI() # 問題数D,最終ゴールG
bPoint = [] # 単体の得点
bCount = [] # 単体の問題数
fPoint = [] # 全問回答時のボーナス
for d in range(0,D):
    bPoint.append((d+1)*100)
    bC,fP = MI()
    bCount.append(bC)
    fPoint.append(fP)

def solver():
    ans = MAXSIZE
    # bit全探索実施
    for bit in range(0,1<<D):
        total = 0
        gets = 0
        selectP=[]
        unselectP=[]
        for x in range(0,D):
            selectFlag=((bit >> x) & 1)
            if selectFlag:
                selectP.append(x)
            else:
                unselectP.append(x)
        unselectP.reverse()
        for t in selectP:
            total=total+bPoint[t]*bCount[t]+fPoint[t]
            gets = gets+bCount[t]
        if G <= total:
            if gets < ans:
                ans = gets
        else:
            unsel = unselectP[0]
            okflag=False
            for count in range(0,bCount[unsel]):
                total = total+bPoint[unsel]
                gets = gets+1
                if G <= total:
                    if gets < ans:
                        ans = gets
                        okflag=True
                    break

    return ans

minCount = solver()
print(minCount)
