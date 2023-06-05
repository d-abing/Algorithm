import sys
input = sys.stdin.readline

T = int(input())

fibonacci_list = [0, 1]

def fibonacci(n):
    if n < len(fibonacci_list):
        return fibonacci_list[n]
    else:
        for i in range(len(fibonacci_list), n + 1):
            fibonacci_list.append(fibonacci_list[i - 1] + fibonacci_list[i - 2])
        return fibonacci_list[n]

def get_0_1_count(N):
    if N == 0:
        count_0 = 1
        count_1 = fibonacci(N)
    else:
        count_0 = fibonacci(N - 1)
        count_1 = fibonacci(N)
    print(count_0, count_1)

for _ in range(T):
    get_0_1_count(int(input()))
