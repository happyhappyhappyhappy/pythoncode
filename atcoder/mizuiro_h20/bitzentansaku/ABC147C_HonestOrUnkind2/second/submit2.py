# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
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
# Const
MAXSIZE = ( 1 << 59 ) -1
MINSIZE = -( 1 << 59) + 1

N = II()
KIND = list()
LIAR = list()
for _ in range(0,N):
    a = II()
    K = list()
    L = list()
    for _ in range(0,a):
        who,said = MI()
        if said == 1:
            K.append(who-1)
        else:
            L.append(who-1)
    KIND.append(K)
    LIAR.append(L)
xdebug("親切テーブル:{}".format(KIND))
xdebug("ウソつきテーブル:{}".format(LIAR))

def solver():
    ans = 0
    for bit in range(1,1<<N):
        xdebug("---ただ今 コード {} の検証---".format(bit))
        honestCL=[]
        liarCL=[]
        for s in range(0,N):
            HF = (bit >> s) & 1
            if HF == 1:
                honestCL.append(s)
            else:
                liarCL.append(s)
        xdebug("検証 正直物のパターン {}".format(honestCL))
        xdebug("    ウソつきのパターン {}".format(liarCL))

        ok = True
        for j in honestCL:
            per = j
            sayHonest = KIND[per]
            sayLiar = LIAR[per]
            xdebug("正直者 {}について".format(per))
            xdebug("正 = {} , うそつき = {}の妥当性を調べる".
                    format(sayHonest,sayLiar))

            for sH in sayHonest:
                if (sH in liarCL):
                    xdebug("{} が正直だという {} は うそつきリスト {}に含まれるのでダメ"
                           .format(j,sH,liarCL))
                    ok=False
            for sL in sayLiar:
                if (sL in honestCL):
                    xdebug("{} がウソつきだという {} は 正直リスト{}に含まれるのでダメ"
                           .format(j,sL,honestCL))
                    ok=False
        if ok:
            if ans < len(honestCL):
                ans = len(honestCL)
            xdebug("このパターンには矛盾がない")
        else:
            xdebug("このパターンには矛盾がある")
    return ans

mx = solver()
print(mx)
