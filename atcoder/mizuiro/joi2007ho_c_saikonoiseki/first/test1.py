N = int(input())
lists = [None for j in range(N)]
tuples = [None for j in range(N)]
for j in range(N):
    strCom = input()
    lists[j] = list(map(int,strCom.split()))
    tuples[j] = tuple(map(int,strCom.split()))
print("{}".format(lists))
print("{}".format(tuples))
lists.sort()
tuples.sort()
print("{}".format(lists))
print("{}".format(tuples))
