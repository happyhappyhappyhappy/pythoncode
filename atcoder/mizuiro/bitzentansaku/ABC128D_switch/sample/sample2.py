from itertools import product

N, M = map(int, input().split())
k_switches = [list(map(int, input().split())) for i in range(M)]
P = list(map(int, input().split()))


def lit_or_not(product, k_switches):
    check = []
    for i in range(M):
        num_of_on = 0
        for j in range(k_switches[i][0]):
            if product[k_switches[i][j + 1] - 1] == 1:
                num_of_on += 1
        if num_of_on % 2 == P[i]:
            check.append(True)
        else:
            check.append(False)

    if all(check):
        return True
    else:
        return False


num_of_matched_products = 0
for i in product((0, 1), repeat=N):
    if lit_or_not(i, k_switches):
        num_of_matched_products += 1
print(num_of_matched_products)
