import sys
# from collections import defaultdict
# import heapq,copy
import pprint as pp
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

# Const
MAXSIZE = ( 1 << 31 ) -1
MINSIZE = -( 1 << 31) + 1

def getValueDef(num,entl,exitl):
    for j in range(num):
        ent,exit = MI()
        entl.append(ent)
        exitl.append(exit)

def fromAtoB(person,entl,extl):
    sum = 0
    for j in range(person):
        sum = sum + abs(entl[j]-extl[j])
    return sum

def getMinDis(num,nowlist):
    posIndex = (num // 2)
    sum = 0
    for j in range(num):
        sum = sum + abs(nowlist[j]-nowlist[posIndex])
    return sum

if __name__ == "__main__":
    person_num = II()
    ent_list = []
    exit_list = []
    getValueDef(person_num,ent_list,exit_list)
    eachsum = fromAtoB(person_num,ent_list,exit_list)
    ent_list.sort()
    exit_list.sort()
    ent_min = getMinDis(person_num,ent_list)
    exit_min = getMinDis(person_num,exit_list)
    final_ans = eachsum+ent_min+exit_min
    print("{}".format(final_ans))
