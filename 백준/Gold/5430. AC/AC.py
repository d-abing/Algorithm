import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    P = input().rstrip()
    n = int(input())
    A = deque(eval(sys.stdin.readline()))

    reverse_flag = False
    left, right = 0, len(A)
    error_raised = False

    for p in P:
        if p == 'R':
            reverse_flag = not reverse_flag
        elif p == 'D':
            if left == right:
                error_raised = True
                print("error")
                break
            if reverse_flag:
                right -= 1
            else:
                left += 1

    if not error_raised:
        result = list(A)[left:right]
        if reverse_flag:
            result.reverse()

        print("[", end='')
        print(*result, sep=',', end='')
        print("]")