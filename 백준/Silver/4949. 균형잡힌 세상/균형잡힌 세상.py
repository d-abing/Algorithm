import sys
input = sys.stdin.readline

while True:
    vps = input()[:-1]
    if vps != '.':
        stack = []
        isvps = True
        for v in vps:
            if v == '(':
                stack.append(1)
            elif v == ')':
                if stack and stack[-1] == 1:
                    stack.pop()
                else:
                    isvps = False
                    break
            elif v == '[':
                stack.append(2)
            elif v == ']':
                if stack and stack[-1] == 2:
                    stack.pop()
                else:
                    isvps = False
                    break
        if stack  or not isvps:
            print("no")
        else:
            print("yes")
    else:
        break
