while True:
    n = int(input())
    if n == -1:
        break

    factors = []
    str_factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)
            str_factors.append(str(i))

    if n == sum(factors):
        print(n, '=', ' + '.join(str_factors))
    else:
        print(n, 'is NOT perfect.')
        