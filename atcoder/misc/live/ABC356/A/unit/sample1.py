n, l, r = map(int, input().split())

n_list = list(range(1, n+1))

tgt_inv = n_list[l-1:r]
tgt_inv.reverse()

n_list_a = n_list[:l-1]
n_list_b = n_list[r:]
print(f"A1={n_list_a},A2={tgt_inv},A3={n_list_b}")
res = n_list_a + tgt_inv + n_list_b

print(" ".join(map(str, res)))
