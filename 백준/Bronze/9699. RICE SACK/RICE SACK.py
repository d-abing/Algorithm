N = int(input())

for i in range(1, N + 1):
    S = list(map(int, input().split()))
    print("Case #{}: {}".format(i, max(S)))