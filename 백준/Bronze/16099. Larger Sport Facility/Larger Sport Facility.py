import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    lt, wt, le, we = map(int, input().split())
    t = lt * wt
    e = le * we
    if t < e:
        print("Eurecom")
    elif t > e:
        print("TelecomParisTech")
    else:
        print("Tie")