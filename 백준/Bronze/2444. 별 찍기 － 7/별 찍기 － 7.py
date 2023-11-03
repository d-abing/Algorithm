N = int(input())

for i in range(1, (2 * N) + 1):
    if i <= N:
        result = ' ' * (N - i) + '*' * ((i - 1) * 2 + 1)
    else:
        result = ' ' * (i - N) + '*' * (((N - (i - N)) - 1) * 2 + 1)
    print(result)
