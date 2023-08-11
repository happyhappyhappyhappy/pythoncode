from collections import defaultdict

d = defaultdict(lambda: defaultdict(int))
d['key']['a']=d['key']['a']+3
print(d)
