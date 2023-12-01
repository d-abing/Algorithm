import sys
import math

input = sys.stdin.readline

while True:
    num = int(input())
    if num == 0:
        break
    else:
        min = num + 1
        max = num * 2
        A = [0] * (max + 1)

        for i in range(min, max + 1):
            A[i] = i

        for i in range(2, int(math.sqrt(max)) + 1):
            for j in range(2 * i, max + 1, i):
                A[j] = 0

        count = 0
        for a in A:
            if a != 0:
                count += 1

        print(count)
