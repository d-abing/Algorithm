n = int(input())
if n == 1:
    print(0)
else:
    count = 0
    for i in range(1, n):
        count += i
    print(count)
print(2)