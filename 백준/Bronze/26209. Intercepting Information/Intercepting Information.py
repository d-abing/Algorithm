S = list(map(int, input().split()))
is_success = True
for s in S:
    if s == 9:
        is_success = False
if is_success:
    print("S")
else:
    print("F")