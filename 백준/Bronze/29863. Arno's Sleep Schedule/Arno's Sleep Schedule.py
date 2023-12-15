sleep = int(input())
if sleep < 4:
    sleep += 24
wake_up = int(input()) + 24

print(wake_up - sleep)