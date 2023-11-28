import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    order = input().split()
    if len(order) == 1:
        if order[0] == '2':
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif order[0] == '3':
            print(len(stack))
        elif order[0] == '4':
            if stack:
                print(0)
            else:
                print(1)
        elif order[0] == '5':
            if stack:
                print(stack[-1])
            else:
                print(-1)
    else:
        stack.append(order[-1])
