import sys
input = sys.stdin.readline

S = [input()[:-1] for _ in range(5)]

for i in range(15):
    has_read = False
    for s in S:
        if len(s) > i:
            print(s[i], end='')
            has_read = True

    if not has_read:
        break
