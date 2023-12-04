import sys
import math
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    num = int(input())
    if num <= 2:
        print("2")
    else:
        while True:
            isPrime = True
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    isPrime = False
                    break
            if isPrime:
                print(num)
                break
            num += 1
