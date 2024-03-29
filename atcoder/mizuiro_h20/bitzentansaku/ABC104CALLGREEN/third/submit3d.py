# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
# from collections import deque
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

D,G = MI()
BaseData=[]
for j in range(0,D):
    a,b = MI()
    BaseData.append([a,(j+1)*100,b])
# print(BaseData)
ans = MAXSIZE
for bit in range(0,1<<D):
    passP = []
    notpassP = []
    for j in range(0,D):
        x = (bit >> j) & 1
        if x == 1:
            passP.append(j)
        else:
            notpassP.append(j)
    # xdebug(f"bit={bit},全完={passP},手つかず={notpassP}")
    nowsum = 0
    nowpass = 0
    # 全完完了問題の計算
    if len(passP)!=0:
        ps = len(passP)
        for j in range(0,ps):
            np = passP[j] # 今全完した問題
            thissum = BaseData[np][0]*BaseData[np][1]+BaseData[np][2]
            nowsum=nowsum+thissum
            nowpass=nowpass+BaseData[np][0]
    # xdebug(f"指定問題 {passP} 全完時-> 合計得点 {nowsum} : 合計問題 {nowpass}")
    # xdebug(f"合格点{G}に満たすか")
    if G <= nowsum:
        # xdebug(f"{G} <= 全完 {passP}の時はここで終了 飛ばします")
        if nowpass <= ans:
            ans = nowpass
            # xdebug(f"ansを{nowpass}にします")
            # xdebug(f"問題数 {ans} になりました")
        continue
    else:
        # notpassPの一番ラストの問題を全部解くまで調べる
        notpassP.reverse()
        # xdebug(f"まだ解いていない{notpassP}の一番最初を解く")
        prob=notpassP[0]
        coun,point,tmp=BaseData[prob]
        # xdebug(f"{prob} 番目情報 全問題数 {coun}問,得点{point}")
        for j in range(0,coun):
            nowsum=nowsum+point
            nowpass=nowpass+1
            if G<=nowsum:
                # xdebug(f"{nowsum}点となり完了しました")
                if nowpass < ans:
                    ans = nowpass
                    # xdebug(f"ansを{nowpass}にします")
                    # xdebug(f"問題数 {ans} になりました")
                # xdebug(f"bit={bit}の時の補講は終了しました")
                break
        # xdebug(f"bit={bit}の時の処理を終了しました")
        continue
print(ans)
