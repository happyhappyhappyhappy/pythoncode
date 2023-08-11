# 英小文字で構成されたランダム文字列
import random
import string
n = 100
val_str="".join([random.choice(string.ascii_lowercase) for _ in range(0,n) ])
print(val_str)

d = {}
print(type(d))
for key in val_str:
    if key not in d:
        d[key]=0
    d[key] = d[key]+1
print(d)
