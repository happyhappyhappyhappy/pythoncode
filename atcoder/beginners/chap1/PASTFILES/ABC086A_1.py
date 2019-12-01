# Problem 
# Python 1st Try
a,b = map(int,input().split(' '))
mods = (a*b)%2
answer = ''
if mods == 0:
    answer = "Even"
else:
    answer = "Odd"
print(answer)