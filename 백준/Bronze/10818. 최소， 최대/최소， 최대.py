import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

print(min(numbers), end=' ')
print(max(numbers))
