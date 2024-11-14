# q(2番目)で割って r(3番目) 余る日に 回収するゴミを d(1番目) 日以降に捨てる

def basic(d,q,r):
    dr=d-r
    print(f"まず 変数の中身{d}から余り{r}を引いたのが {dr}")
    kiriage=(dr+q-1)//q
    print(f"{dr}を{q}で割った場合に切り上げたのが{kiriage}")
    r0=kiriage*q
    print(f"もし余りが0ならば{r0}")
    res=r0+r
    return res


q=7 # 回収周期->qで割った余りに関連する
r=3 # プラス余り->普通は0だが今回は余りも絡む
d=15 # 提出日->変数
x=basic(d,q,r)
print(f"余り0に余りを加えると{x}")
