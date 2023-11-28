import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    vps = input()[:-1]
    stack = []
    isvps = True
    for v in vps:
        if v == '(':
            stack.append(1)
        else:
            if stack:
                stack.pop()
            else:
                isvps = False
                break
    if stack or not isvps:
        print("NO")
    else:
        print("YES")
