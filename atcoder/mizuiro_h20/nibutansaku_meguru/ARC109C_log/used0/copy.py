def is_ok(L):
    print(f"---- {L} ----の場合")
    result = False
    countLeng = ((L+1)*L)//2
    # print(f"長さ{L} だと合計の長さが {countLeng}になる")
    print(f"1+2+...+(k={L})={countLeng} <= N+1={N+1}(お店にある丸太の最大)")
    if countLeng <= N+1:
        print(f"これは一応ながら条件式を満たす")
        result = True
    else:
        print(f"これは長過ぎ満たさない->NG")
    return result
def meguru_bisect(ng,ok):
    while(1 < abs(ok-ng)):
        mid = (ok+ng)//2
        if is_ok(mid):
            print(f"1...{mid}は売っている材木から切り出せる のでさらに値を {ok}->{mid}に上げる")
            ok = mid
        else:
            print(f"1...{mid}は売っている材木から切り出せないので 値を{ng}->{mid}に下げる")
            ng=mid
    print(f"{ok}がこの二部検索に最後に求める値")
    return ok

N = int(input())
print(f"1...{N+1}までの丸太から一本ずつ->1...{N}を切り出せる本数は")

X = meguru_bisect(10**20,0)
print(f"長さN+1(={N+1})の丸太一本で1...{X}までの{X}本 切り出せる")
print(f"結果 1...{N}の丸太を 一本ずつ切り出せる買い方は")
print(f"まずN+1(={N+1})の長さの丸太を買う->1")
print(f"これで1...{X}まで{X}本切り出せる")
print(f"あとは{X+1}..{N}の丸太を1本づつ買う-> N-X={N-X}")
print(f"1+{N-X}")
print((N+1)-X)
