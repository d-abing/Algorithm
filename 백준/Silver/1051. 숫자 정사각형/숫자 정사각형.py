from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
numbers = list()
for i in range(N):
    numbers.append(input()[0:-1])

length = 0
size = 1

for j, line in enumerate(numbers):
    for k, number in enumerate(line):
        limit = M
        while line[:limit].count(number) > 1:
            index_left = k
            index_right = line[:limit].rfind(number)
            if index_right - index_left > length:
                tmp_length = index_right - index_left
                if (j + tmp_length < N and\
                 numbers[j + tmp_length][index_left] == number and numbers[j + tmp_length][index_right] == number) or\
                    (j - tmp_length >= 0 and\
                    (numbers[j - tmp_length][index_left] == number and numbers[j - tmp_length][index_right] == number)):
                    length = tmp_length
                    size = (length + 1) ** 2
            limit -= 1

print(size)