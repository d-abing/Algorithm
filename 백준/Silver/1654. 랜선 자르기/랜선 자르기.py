import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lengths = [int(input()) for _ in range(K)]

s = 1
e = max(lengths)
count = 0

while s <= e:
    m = (s + e) // 2
    count = 0
    for length in lengths:
        count += length // m
    if count >= N:
        s = m + 1
    elif count < N:
        e = m - 1

print(e)
