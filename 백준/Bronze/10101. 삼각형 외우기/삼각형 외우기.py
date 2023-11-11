angles = [int(input()) for _ in range(3)]

if sum(angles) == 180:
    max_count = 0
    for angle in angles:
        max_count = angles.count(angle) if angles.count(angle) > max_count else max_count
    if max_count == 1:
        print('Scalene')
    elif max_count == 2:
        print('Isosceles')
    else:
        print('Equilateral')
else:
    print('Error')