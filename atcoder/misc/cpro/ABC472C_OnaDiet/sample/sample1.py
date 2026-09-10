N, M, K = map(int, input().split())
A = list(map(int, input().split()))
s = 0
for i in range(N):
  print(f"{i}日目")
  if M <= i:
    print(f"i={i},M={M}->sから {i-M}日目のデータを取り除きます")

    s = s - A[i - M]
  if s + A[i] <= K:
    print(f"K={K}以内")
    s += A[i]
    print("Yes")
  else:
    print(f"それ以外 {i}日目は食べません")
    A[i] = 0
    print("No")
    print(f"A={A}")
