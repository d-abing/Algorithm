import sys
input = sys.stdin.readline

N = int(input())
set = set()
has_entered = False
result = 0

for _ in range(N):
    log = input()[:-1]
    if log == 'ENTER':
        has_entered = True
        result += len(set)
        set.clear()
    else:
        set.add(log)

result += len(set)

print(result)