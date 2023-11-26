A = list(map(int, input().split()))

for i in range(1, 100 ** 3):
    count = 0
    for a in A:
        if i % a == 0:
            count += 1
    if count >= 3:
        print(i)
        break