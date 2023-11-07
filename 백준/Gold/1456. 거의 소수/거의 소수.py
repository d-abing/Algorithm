import sys
import math
input = sys.stdin.readline

A, B = map(int, input().split())
prime_numbers = [num for num in range(10_000_001)]
prime_numbers[1] = 0

for i in range(int(math.sqrt(len(prime_numbers) - 1)) + 1):
    if prime_numbers[i] == 0:
        continue
    for j in range(2 * i, len(prime_numbers), i):
        prime_numbers[j] = 0

count = 0

for i in range(2, int(math.sqrt(B)) + 1):
    if prime_numbers[i] != 0:
        prime_number = i ** 2
        while prime_number <= B:
            if prime_number >= A:
                count += 1
            prime_number *= i

print(count)
