N, M = map(int, input().split())
for _ in range(N):
    S = input().strip()
    print(S[-1:-(len(S) + 1):-1])