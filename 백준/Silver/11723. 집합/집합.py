import sys
input = sys.stdin.readline

M = int(input())
S = []

for _ in range(M):
    operation = input().split()
    if operation[0] == 'add':
        if S.count(operation[1]) == 0:
            S.append(operation[1])
    elif operation[0] == 'remove':
        if S.count(operation[1]) != 0:
            S.remove(operation[1])
    elif operation[0] == 'check':
        if S.count(operation[1]) == 0:
            print(0)
        else:
            print(1)
    elif operation[0] == 'toggle':
        if S.count(operation[1]) == 0:
            S.append(operation[1])
        else:
            S.remove(operation[1])
    elif operation[0] == 'all':
        S = [str(i) for i in range(1, 20 + 1)]
    elif operation[0] == 'empty':
        S = []
