from collections import defaultdict
import pickle
d = {'a':10,'b':20}
with open('dick.pickle','wb') as f:
    pickle.dump(d,f)
