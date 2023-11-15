N = int(input())
M = int(input())
buttons = [i for i in range(10)]
wrong_button = []
if M != 0:
    wrong_buttons = list(map(int, input().split()))
    for wrong_button in wrong_buttons:
        if wrong_button in buttons:
            buttons.remove(wrong_button)


if len(buttons) != 0:
    str_N = str(N)
    min_channel = ''
    max_channel = ''

    for n in str_N:
        min_error = 10
        max_error = 10
        min_s = '-'
        max_s = '-'
        for button in buttons:
            if abs(button - int(n)) < min_error and button <= int(n):
                min_error = abs(button - int(n))
                min_s = str(button)
            if abs(button - int(n)) < max_error and button >= int(n):
                max_error = abs(button - int(n))
                max_s = str(button)
        min_channel += min_s
        max_channel += max_s


    def min_convert(channel):
        for i in range(len(channel)):
            if channel[i] == '-':
                if i == 0:
                    channel = '0' * len(channel)
                else:
                    pre_num = 0
                    for button in reversed(buttons):
                        if int(channel[i - 1]) > button:
                            pre_num = button
                            break
                    return int(channel[:i - 1] + str(pre_num) + str(max(buttons)) * (len(channel) - i))

            if str_N[i] == channel[i]:
                if i != len(channel) - 1:
                    continue
                return int(channel)
            elif str_N[i] > channel[i]:
                return int(channel[:i + 1] + str(max(buttons)) * (len(channel) - (1 + i)))


    def max_convert(channel):
        for i in range(len(channel)):
            if channel[i] == '-':
                if i == 0:
                    if len(buttons) == 1:
                        min_button = str(min(buttons))
                    else:
                        min_button = str(min(buttons)) if min(buttons) != 0 else str(buttons[1])
                    return int(min_button + str(min(buttons)) * len(channel))
                else:
                    next_num = 0
                    for button in buttons:
                        if int(channel[i - 1]) < button:
                            next_num = button
                            break
                    return int(channel[:i - 1] + str(next_num) + str(min(buttons)) * (len(channel) - i))

            if str_N[i] == channel[i]:
                if i != len(channel) - 1:
                    continue
                return int(channel)
            elif str_N[i] < channel[i]:
                return int(channel[:i + 1] + str(min(buttons)) * (len(channel) - (1 + i)))

    converted_min = min_convert(min_channel) if min_convert(min_channel) != 0 else min(buttons)
    converted_max = max_convert(max_channel) if max_convert(max_channel) != 0 else max(buttons)

    result1 = abs(N - converted_min) + len(str(converted_min))
    result2 = abs(N - converted_max) + len(str(converted_max))
    result3 = abs(N - 100)

    print(min(result1, result2, result3))

else:
    print(abs(N - 100))
