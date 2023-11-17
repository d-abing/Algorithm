N, m, M, T, R = map(int, input().split())

time = 0
pulse = m
value = 0
can_practice = True
while N > 0:
    value = -R
    if pulse + T <= M:
        value = T
        N -= 1
    elif pulse - R < m:
        value = m - pulse
    if value == 0:
        can_practice = False
        print(-1)
        break
    pulse += value
    time += 1

if can_practice:
    print(time)
