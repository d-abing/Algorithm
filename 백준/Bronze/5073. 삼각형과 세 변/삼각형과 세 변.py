while True:
    lengths = list(map(int, input().split()))
    if sum(lengths) == 0:
        break

    lengths.sort()
    if lengths[0] + lengths[1] <= lengths[2]:
        print('Invalid')
    else:
        max_count = 0
        for length in lengths:
            max_count = lengths.count(length) if lengths.count(length) > max_count else max_count
        if max_count == 1:
            print('Scalene')
        elif max_count == 2:
            print('Isosceles')
        else:
            print('Equilateral')