N = int(input())
X = []
Y = []
for _ in range(N):
    a, b = map(int, input().split())
    X.append(a)
    Y.append(b)

print((max(X) - min(X)) * (max(Y) - min(Y)))
