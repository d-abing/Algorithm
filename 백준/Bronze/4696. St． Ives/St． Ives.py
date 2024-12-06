while True:
    N = float(input())
    if N == 0:
        break

    answer = 0
    for i in range(5):
        answer += N ** i

    st_answer = "{:.2f}".format(answer)

    print(st_answer)