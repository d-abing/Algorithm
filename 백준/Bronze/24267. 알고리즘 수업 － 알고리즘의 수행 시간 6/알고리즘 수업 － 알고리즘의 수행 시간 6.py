n = int(input())
if n < 3:
    print(0)
else:
    A = [i for i in range(1, 500000 + 1)]
    prefix_sum = [0]

    for i in range(500000):
        prefix_sum.append(prefix_sum[i] + A[i])

    print(sum(prefix_sum[:n - 1]))
print(3)