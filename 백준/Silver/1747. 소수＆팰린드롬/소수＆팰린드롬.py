import math

N = int(input())

prime_numbers = [i for i in range(1_003_002)]
prime_numbers[1] = 0

for i in range(2, int(math.sqrt(len(prime_numbers) - 1)) + 1):
    if prime_numbers[i] == 0:
        continue
    for j in range(2 * i, len(prime_numbers), i):
        prime_numbers[j] = 0


def is_palindrome(num):
    str_num = str(num)
    for i in range(len(str_num) // 2):
        if str_num[i] != str_num[-(i + 1)]:
            return False
    return True


for number in prime_numbers:
    if number != 0 and number >= N and is_palindrome(number):
        print(number)
        break
