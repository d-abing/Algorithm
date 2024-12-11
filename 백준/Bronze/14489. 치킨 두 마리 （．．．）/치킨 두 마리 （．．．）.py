A, B = map(int, input().split())
C = int(input())

if A + B >= C * 2:
    print(A + B - C * 2)
else:
    print(A + B)