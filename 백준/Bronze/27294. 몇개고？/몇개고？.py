T, S = map(int, input().split())
if S == 0:
    if 12 <= T <= 16:
        print("320")
    else:
        print("280")
else:
    print("280")