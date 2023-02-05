ZIPS = list(zip([1,2,3,4,5],["a","b","c","d"]))
print("ZIPS type = {}".format(type(ZIPS)))
#  <class 'list'>
print("ZIPS IN = {}".format(ZIPS))
# ZIPS IN = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
cnt = 1
for z in ZIPS:
    print("{} : {}".format(cnt,z))
#     1 : (1, 'a')
# 2 : (2, 'b')
# 3 : (3, 'c')
# 4 : (4, 'd')
    cnt = cnt+1
r1 = range(0,3)
l1 = ['fee','fit','for','fim']
ZIPS2 = list(zip(r1,l1))

print("ZIPS2 type={}".format(type(ZIPS2)))
# <class 'list'>
print("ZIPS2 in ={}".format(ZIPS2))# for t in ZIPS:
# [(0, 'fee'), (1, 'fit'), (2, 'for')]
lines=list()

# 二次元配列として作成
r1list=list(r1)
lines.append(r1list)
lines.append(l1)
print(lines)
# [[0, 1, 2], ['fee', 'fit', 'for', 'fim']]
linezip = list(zip(*lines))
print("linezip type={}".format(type(linezip)))
# linezip type=<class 'list'>
print("linezip in = {}".format(linezip))
# linezip in = [(0, 'fee'), (1, 'fit'), (2, 'for')]
