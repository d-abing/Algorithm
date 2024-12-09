a, b = map(int, input().split())

if a % 2 == 0 or b % 2 == 0:
    print(0)
else:
    if a > b:
        print(b)
    else:
        print(a)