A, B = map(int, input().split())

max_value = max(A, B)
min_value = min(A, B)
while max_value % min_value != 0:
    remainder = max_value % min_value
    max_value = min_value
    min_value = remainder

for _ in range(min_value):
    print('1', end='')
