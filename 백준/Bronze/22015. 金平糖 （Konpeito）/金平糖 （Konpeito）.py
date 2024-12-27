A, B, C = map(int, input().split())
max_count = max(A, B, C)
print(3 * max_count - (A + B + C))