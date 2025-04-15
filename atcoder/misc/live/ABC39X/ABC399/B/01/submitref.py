import sys
from logging import DEBUG, StreamHandler, getLogger

def II(): return int(sys.stdin.readline())
def LI(): return list(map(int, sys.stdin.readline().split()))

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

xdebug = logger.debug

def solve():
    N = II()
    A = LI()
    res = [-1] * N
    rank = 1  # 順位を管理する変数をrankに変更

    while -1 in res:
        max_val = -1
        for i in range(N):
            if res[i] == -1 and A[i] > max_val: #最大値の更新条件を見直し
                max_val = A[i]

        count = 0
        for i in range(N):
            if A[i] == max_val:
                res[i] = rank
                count += 1
        rank += count #順位の更新
    return res

if __name__ == "__main__":
    result = solve() #変数名をresからresultに変更
    for r in result: #変数名をxからrに変更
        print(r)
