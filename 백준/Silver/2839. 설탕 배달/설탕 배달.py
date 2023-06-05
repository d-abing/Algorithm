import sys
input = sys.stdin.readline

N = int(input())
count = -1

if N % 5 == 0:
    count = N / 5
else:
    for i in range(0, N // 3):
        if (N - (3 * i)) % 5 == 0:
            fiveCount = (N - (3 * i)) // 5
            count = i + fiveCount
            break
        elif N % 3 == 0:
            count = N // 3

print(int(count))