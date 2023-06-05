from sys import stdin
input = stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
good_nums = set()
result = 0

def count_numbers(numbers):
    count_dict = {}
    for number in numbers:
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1

    return count_dict

dict_numbers = count_numbers(numbers)

def remove_values_at_indices(arr, index1, index2):
    new_arr = arr.copy()
    del new_arr[index1]
    del new_arr[index2 - 1]
    return new_arr

def count_good_numbers(numbers):
    count = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] in remove_values_at_indices(numbers, i, j):
                good_nums.add(numbers[i] + numbers[j])

count_good_numbers(numbers)

for num in good_nums:
    if num in dict_numbers:
        result += dict_numbers[num]

print(result)
