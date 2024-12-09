R, C, N = map(int, input().split())
col = row = 0

if R % N != 0:
    col = R // N + 1
else:
    col = R // N

if C % N != 0:
    row = C // N + 1
else:
    row = C // N

print(col * row)