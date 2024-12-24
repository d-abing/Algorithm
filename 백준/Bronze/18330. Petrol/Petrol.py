n = int(input())
k = int(input())

max_1500 = 60 + k

if n - max_1500 >= 0:
    print(max_1500 * 1500 + (n - max_1500) * 3000)
else:
    print(n * 1500)