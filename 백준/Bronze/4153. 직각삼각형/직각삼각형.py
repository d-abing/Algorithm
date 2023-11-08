import sys
input = sys.stdin.readline

while True:
    triangle = list(map(int, input().split()))
    if sum(triangle) == 0:
        break

    triangle.sort()
    is_right = 'wrong'
    if triangle[0] ** 2 + triangle[1] ** 2 == triangle[2] ** 2:
        is_right = 'right'
    print(is_right)
    