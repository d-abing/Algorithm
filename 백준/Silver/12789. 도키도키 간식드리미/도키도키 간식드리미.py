import sys
input = sys.stdin.readline

N = int(input())
orders = list(map(int, input().split()))
orders.reverse()
stack = []

for i in range(1, N + 1):
    if stack and stack[-1] == i:
        stack.pop()
        continue
    while orders:
        number = orders.pop()
        if number == i:
            break
        else:
            stack.append(number)

if stack or orders:
    print("Sad")
else:
    print("Nice")