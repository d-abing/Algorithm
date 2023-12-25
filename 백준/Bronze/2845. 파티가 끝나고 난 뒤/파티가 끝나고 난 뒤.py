L, P = map(int, input().split())
list = list(map(int, input().split()))

for num in list:
    print(num - (L * P), end=' ')