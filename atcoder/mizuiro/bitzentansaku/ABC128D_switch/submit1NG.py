import sys
# from collections import defaultdict
# import heapq,copy
import pprint as pp
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
# main関数から始まるパターンは一旦保留する→スクリプト形式へ

# Const
MAXSIZE = ( 1 << 31 ) -1
MINSIZE = -( 1 << 31) + 1

def solver(Switch,Lamp,G,Echeck):

    for sw_pat in range(1<<Switch):
        swlist = list()
        pushedSwitch = 0
        for shift in range(Switch):
            if ( sw_pat >> shift) & 1:
                swlist.append(True)
                pushedSwitch = pushedSwitch+1
            else:
                swlist.append(False)
        checkOddEven = pushedSwitch % 2
        print("{} の場合の 押されるスイッチ列 {}".format(sw_pat,swlist))
        print("偶奇合わせ : {}".format(checkOddEven))
        # Lamp毎のチェック
        lamp_counter=0
        for lamps in range(Lamp):
            check_counter=0
            print("ランプ {} について".format(lamps))
            use_switch = len(grid[lamps])
            print("関連のあるスイッチは {}".format(grid[lamps]))
            nowLampCheck = True
            for x in range(use_switch):
                # 各ランプで使うスイッチが今ONになっているか確認する
                print("grid[{}][{}] = {}".format(lamps,x,grid[lamps][x]))
                # 多分下の式のgridの値をswitchlistの要素にすれば良いと思う
                if grid[lamps][x] != True:
                    print(" {} のスイッチが押されていないので終了".format(grid[lamps][x]))
                    nowLampCheck = False
                    break
            if nowLampCheck and ( checkOddEven == Echeck[lamps]):
                print("ランプ {} は点灯する".format(lamps))
    # for nowlamp in range(Lamp)
    #     for x in range(2**Switch):
    #         print("bit列 {} の場合".format(x))
    #         sw_count = 0
    #         for shift in range(Switch):
    #             if (x >> shift) & 1:
    #                 sw_count = sw_count+1
    #             print("  スイッチ {} は押されます".format(shift))
    #             else:
    #             print("   スイッチ {} は押されません".format(shift))
    #         print("スイッチ計: {}".format(sw_count))
    result = 0
    # algorithm
    return result


if __name__ == "__main__":
    # 情報入力
    N,M = MI()
    grid=list()
    for x in range(M):
        grid.append(LI())
    even_or_odd = LI()
    # ざっくりと挿入したgridに手を加える
    # 1.各行の1つめは削除する
    for x in range(M):
        grid[x].pop(0)
    # 2.0-indexへ修正する
    for x in range(M):
        y = len(grid[x])
        for z in range(y):
            grid[x][z] = grid[x][z]-1
    print("{}".format(solver(N,M,grid,even_or_odd)))
