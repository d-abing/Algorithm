T = int(input())
for _ in range(T):
    steps = input()
    count = 0
    for s in steps:
        if s == "U":
            count += 1
        elif s == "D":
            break
    print(count)
     