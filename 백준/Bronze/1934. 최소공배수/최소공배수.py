import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    max_value = max(A, B)
    min_value = min(A, B)
    while max_value % min_value != 0:
        remainder = max_value % min_value
        max_value = min_value
        min_value = remainder

    GCD = min_value
    result = A * B // min_value
    print(result)
    