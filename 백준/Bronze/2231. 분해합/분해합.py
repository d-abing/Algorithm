N = int(input())
number = 0
has_found = False

while number <= N:
    str_n = str(number)
    decomposition_sum = 0
    for i in range(len(str_n)):
        decomposition_sum += int(str_n[i])
    decomposition_sum += number
    if decomposition_sum == N:
        print(number)
        has_found = True
        break
    number += 1

if not has_found:
    print(0)