A, B = input().split()
sum = 0
for a in A:
    for b in B:
        sum += int(a) * int(b)
print(sum)