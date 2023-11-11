X = []
Y = []
for _ in range(3):
    a, b = map(int, input().split())
    X.append(a)
    Y.append(b)

for x in X:
    if X.count(x) == 1:
        print(x, end=' ')
for y in Y:
    if Y.count(y) == 1:
        print(y)
        