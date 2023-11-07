T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    Y = N % H if N % H != 0 else H
    X = 1 + (N // H) if N % H != 0 else (N // H)
    str_X = '0' + str(X) if X < 10 else str(X)
    print(str(Y) + str_X)
