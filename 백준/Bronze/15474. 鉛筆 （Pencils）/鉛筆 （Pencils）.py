N, A, B, C, D = map(int, input().split())

X = N // A * B
Y = N // C * D

if N % A != 0:
    X += B

if N % C != 0:
    Y += D

print(min(X, Y))
