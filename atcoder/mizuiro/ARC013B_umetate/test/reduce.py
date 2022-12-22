from functools import reduce
from operator import add
from operator import sub
from operator import mul
from operator import or_

array = [1,2,3,4,5,6]
print("足し算: {}".format(reduce(add,array)))
print("引き算: {}".format(reduce(sub,array)))
print("かけ算: {}".format(reduce(mul,array)))

# orを使って見る
pattarn1 = [0,1,0,1,1]
pattarn2 = [1,1,0,0,1]
