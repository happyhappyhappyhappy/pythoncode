import numpy as np

def func(X):
    print(X)

if __name__ == '__main__':
    a = np.zeros((2, 3))
    func(a)
    a[0][2] = 1
    print(a)
