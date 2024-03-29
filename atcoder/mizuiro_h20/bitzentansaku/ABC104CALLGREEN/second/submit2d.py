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

# デバッグ出力の作成
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

# クラス+メソッドを一関数
xdebug=logger.debug
ppp=pprint.pprint

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

xdebug("問題一問回答時の点数: {}".format(bPoint))
xdebug("各問の問題数: {}".format(bCount))
xdebug("パーフェクトポイント: {}".format(fPoint))

def solver():
    ans = MAXSIZE
    # bit全探索実施
    for bit in range(0,1<<D):
        total = 0
        gets = 0
        xdebug("bit is {}".format(bit))
        selectP=[]
        unselectP=[]
        for x in range(0,D):
            selectFlag=((bit >> x) & 1)
            if selectFlag:
                selectP.append(x)
            else:
                unselectP.append(x)
        unselectP.reverse()
        xdebug("全問問題対象={}".format(selectP))
        xdebug("全問問題対象外={}".format(unselectP))
        for t in selectP:
            total=total+bPoint[t]*bCount[t]+fPoint[t]
            gets = gets+bCount[t]
        if G <= total:
            xdebug("この時 合計 {} 点 / {} 問 : 合格点に満たす".format(total,gets))
            if gets < ans:
                ans = gets
        else:
            xdebug("この時 合計 {} 点 / {} 問: 合格点に満たない".format(total,gets))
            xdebug("未選択のうち1問あたりの成果が高い {} 問目を解いてみる".format(unselectP[0]+1))
            unsel = unselectP[0]
            okflag=False
            for count in range(0,bCount[unsel]):
                total = total+bPoint[unsel]
                gets = gets+1
                if G <= total:
                    xdebug("この時 合計 {} 点 / {} 問 : 合格点に満たす".format(total,gets))
                    if gets < ans:
                        ans = gets
                        okflag=True
                    break
                else:
                    xdebug("まだ 合計 {} 点(目標 {}点)/ {}問 で合格点ではないのでもう一巡してみる".format(total,G,gets))
            if okflag:
                xdebug("この方法で解に見つかった")
            else :
                xdebug("全解き {},部分稼ぎ {}で解は見つからない".format(selectP,unselectP[0]))
        xdebug("全解き: {} , 一旦無視: {}での検証終わり".format(selectP,unselectP))

    return ans

minCount = solver()
print(minCount)
