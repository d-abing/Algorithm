l, r = map(int, input().split())

if l == r == 0:
    print("Not a moose")
elif l == r:
    print("Even {}".format(l + r))
else:
    print("Odd {}".format(max(l, r) * 2))