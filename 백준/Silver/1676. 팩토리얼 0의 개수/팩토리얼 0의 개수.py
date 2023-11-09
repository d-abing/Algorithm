import sys
sys.setrecursionlimit(100000)
N = int(input())
factorial_list = [0] * 501
factorial_list[0:2] = 1, 1


def factorial(N):
    if factorial_list[N] != 0:
        return factorial_list[N]
    else:
        return N * factorial(N - 1)


factorial_result = str(factorial(N))
count = 0
for i in factorial_result[-1:-(len(factorial_result) + 1):-1]:
    if i == '0':
        count += 1
    else:
        print(count)
        break
