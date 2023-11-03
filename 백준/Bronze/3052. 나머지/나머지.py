import sys
input = sys.stdin.readline

remainders = set()

for _ in range(10):
    num = int(input())
    remainders.add(num % 42)

print(len(remainders))
