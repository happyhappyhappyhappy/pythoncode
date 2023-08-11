from collections import defaultdict
import random
import string
n = 100
strlist=[random.choice(string.ascii_lowercase) for _ in range(0,n)]
val_str="".join(strlist)
print(strlist)
print(val_str)
d = defaultdict(list)
print(f"{type(d)}\n")

for key in val_str:
    d[key].append(key)

print(d)
