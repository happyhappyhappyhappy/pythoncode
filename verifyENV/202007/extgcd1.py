# Problem: extend GCD

import sys
import pprint as pp
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def run_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = run_gcd(b % a, a)
        x = x - (b // a) * y
        return g, x, y


if __name__ == "__main__":

    a = int(input())
    b = int(input())
    g, x, y = run_gcd(a, b)
    pp.pprint("g={},x={},y={}".format(g, x, y))
    # print("{}".format(run_gcd()))
