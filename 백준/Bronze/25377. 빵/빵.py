N = int(input())
can_buy_bread = False
time = 1001
for _ in range(N):
    A, B = map(int, input().split())
    if A <= B < time:
        time = B
        can_buy_bread = True

if can_buy_bread:
    print(time)
else:
    print(-1)
