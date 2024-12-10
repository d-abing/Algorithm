friends = list(map(int, input().split()))

if friends.count(0) == 1:
    print(chr(ord("A") + friends.index(0)))
elif friends.count(1) == 1:
    print(chr(ord("A") + friends.index(1)))
else:
    print("*")