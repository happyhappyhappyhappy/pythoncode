import math
import itertools

def gen_primes_upto(n):
    if n==2:
        return
    table = [True]*n
    sqrtn=int(math.ceil(math.sqrt(n)))
    for j in range(2,sqrtn):
        if table[j] == True:
            for k in range(j*j,n,j):
                table[j]=False
    yield 2
    for j in range(3,n,2):
        if table[j]==True:
            yield j

def gen_primes_upto_segmented(n):
