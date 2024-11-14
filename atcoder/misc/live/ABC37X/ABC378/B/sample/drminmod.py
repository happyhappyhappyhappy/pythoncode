# m(2番目) で割って r(3番目) 余る x(1番目) 以上の最小の整数
# q(2番目)で割って r(3番目) 余る日に 回収するゴミを d(1番目) 日以降に捨てる
# x-> d, m-> q
def drminmod(d,q,r):
    print(f"ゴミを出した日{d}から、回収基準余り {r}を引いた物を求めます")
    d=d-r

    rd=(d%q+q)%q
    print(f"d%q+q={d%q+q}とq={q}の余りを求めます")
    if 0 < rd:
        res=d + (q-rd) + r
        print(f"True 回収は {res} 日ですか")
    else:
        res=d+r
        print(f"False 回収は {res} 日ですか")
    return 0


q=7
r=3
d=3
x=drminmod(d,q,r)
print(x)
