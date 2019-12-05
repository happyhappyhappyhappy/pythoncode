# Problem https://atcoder.jp/contests/abc064/tasks/abc064_a
# Python 1st Try
rgbs = list(map(int, input().split(' ')))
g = rgbs[1]
b = rgbs[2]
answer = ''
checkgb = ((g*10+b) % 4)
if checkgb == 0:
    answer = "YES"
else:
    answer = "NO"
print(answer)
