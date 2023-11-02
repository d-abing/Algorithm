N = int(input())


def check_primenumber(num):
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def DFS(num):
    if len(str(num)) == N:
        print(num)
    else:
        for i in range(1, 10, 2):
            if check_primenumber(num * 10 + i):
                DFS(num * 10 + i)


DFS(2)
DFS(3)
DFS(5)
DFS(7)