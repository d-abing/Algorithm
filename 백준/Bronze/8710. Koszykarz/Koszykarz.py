k, w, m = map(int, input().split())
h = w - k

if h % m == 0:
    print(h // m)
else:
    print(h // m + 1)