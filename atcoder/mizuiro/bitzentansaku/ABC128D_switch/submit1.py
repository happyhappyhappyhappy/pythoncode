import sys
# from collections import defaultdict
# import heapq,copy
from logging import getLogger, StreamHandler, DEBUG
# import pprint as pp
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

# logger.debug('デバッグの例')

# Const
MAXSIZE = ( 1 << 31 ) -1
MINSIZE = -( 1 << 31) + 1

N,M = MI() # N->スイッチ M->ランプ
G = list()
for x in range(M):
    G.append(LI())
ODDCHECK = LI()

# 加工
# 各行先頭を削る
for x in range(M):
    G[x]=G[x][1:]
    # 他に G[x].pop(0)
    # del G[x][0]
# print(G)
for x in range(M):
    x_Length = len(G[x])
    for y in range(x_Length):
        G[x][y] = G[x][y]-1
result = 0

for switch_pattern in range(1<<N):
# 各スイッチパターン毎の初期情報
    switch_onofflist = list() # switchのON/OFFチェックリスト
    switch_cnt = 0
    # switch_onofflistの内容作成
    for bit_shift in range(N):
        if (switch_pattern >> bit_shift) & 1:
            switch_onofflist.append(True)
            switch_cnt = switch_cnt+1
        else:
            switch_onofflist.append(False)
    # 押されているswitchの数が奇数か否か
    logger.debug(switch_onofflist)
# ランプ毎にこのスイッチパターンで付くか否か確認
# 付いているランプの数
    on_lamp = 0
    for lamp in range(M):
        logger.debug("ランプ {} について".format(lamp))
        switch_count=0
        this_lamp_on = True
        for j in range(len(G[lamp])):
            if switch_onofflist[G[lamp][j]] == False:
                this_lamp_on = False
            else:
                switch_count = switch_count+1
        if this_lamp_on == True:
            logger.debug("ランプ = {} についてスイッチ条件が満たされたので奇数か確認します"\
                    .format(lamp))
            logger.debug("今の押されているスイッチの個数は{}".format(switch_cnt))
            if (switch_cnt%2) == ODDCHECK[lamp]:
                logger.debug("間違いなく付きます")
                on_lamp = on_lamp+1
    logger.debug("全ランプ {} に対して点灯した数 {}".\
        format(M,on_lamp))
    if on_lamp == M:
        logger.debug("スイッチ {} の時全部付きます".format(switch_onofflist))
        result = result+1
print(result)
