import sys
input = sys.stdin.readline

N = int(input())
print("Gnomes:")
for _ in range(N):
    sq = list(map(int, input().split()))
    if sq == sorted(sq) or sq == sorted(sq, reverse=True):
        print("Ordered")
    else:
        print("Unordered")