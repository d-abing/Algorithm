sticks = list(map(int, input().split()))
sticks.sort()

if sticks[0] == sticks[1] == sticks[2]:
    print(2)
elif sticks[0] ** 2 + sticks[1] ** 2 == sticks[2] ** 2:
    print(1)
else:
    print(0)