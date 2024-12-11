meat = [ int(input()) for _ in range(5) ]


if meat[0] < 0:
    print(abs(meat[0]) * meat[2] + meat[3] + meat[1] * meat[4])
else:
    print((meat[1] - meat[0]) * meat[4])