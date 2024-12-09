count = 0

while True:
    count += 1

    median_list = list(map(float, input().split()))

    if median_list == [0]:
        break

    len_of_list = int(median_list[0])
    answer = 0

    if len_of_list % 2 == 0:
        answer = (median_list[len_of_list // 2] + median_list[len_of_list // 2 + 1]) / 2
    else:
        answer = median_list[len_of_list // 2 + 1]

    print("Case {}: {:.1f}".format(count, answer))