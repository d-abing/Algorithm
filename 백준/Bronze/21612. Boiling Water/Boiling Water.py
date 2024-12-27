B = int(input())
T = 5 * B - 400
print(T)
if T > 100:
    print(-1)
elif T < 100:
    print(1)
else:
    print(0)