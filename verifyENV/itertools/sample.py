from itertools import product
import pprint

xprint=pprint.pprint

l1 = ['a','b','c']
l2 = ['X','Y','Z']

p = product(l1,l2)
print("基本情報")
print(p)

print(type(p))

print("タプル出力する")
for v in p:
    print(v)
print("もう一回")
for v in p:
    print(v) # 何も出ない
print("分けて出力する")
p2 = product(l1,l2)
for v1,v2 in p2:
    print("{}-{}".format(v1,v2))
print("二重ループにする")
for v1 in l1:
    for v2 in l2:
        print("{}-{}".format(v1,v2))
print("リスト化")
l_p = list(product(l1,l2))
pprint.pprint(l_p)

# キーワード引数にRepeatを使う
print("キーワード引数にRepeatを使う")
l3=[0,1]
# l3_p=list(product(l3,repeat=3))
l3_p=list(product(l3,repeat=3))
pprint.pprint(l3_p)
print("この方法と同じ")
l3_p2=list(product(l3,l3,l3))
xprint(l3_p2)

print("複数を利用する")
l41=[0,1]
l42=[2,3]
# list(product(l41,l42,repeat=3))
l4_p=list(product(l41,l42,repeat=3))
xprint(l4_p)
