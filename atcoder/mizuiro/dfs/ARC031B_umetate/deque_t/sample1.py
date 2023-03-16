from collections import deque
n = 10
m = 5
mystack = deque(list())
mystack.append([n,m])
n = 22
m = 11
mystack.append([n,m])
print(" now mystack len = {} ".format(len(mystack)))
xl = mystack.pop()
print(" 多分 [22,11] が出るはず {}".format(xl))
xl2 = mystack.pop()
print(" 多分 [10,5] が出るはず {}".format(xl2))
print(" now mystack len = {} ".format(len(mystack)))
