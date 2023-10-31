N = int(input())

list = [int(input()) for _ in range(N)]
list.sort()

for num in list:
    print(num)