N = int(input())

for _ in range(N):
    data = str(input())
    answer = ""

    for i in range(len(data)):
        if i == 0 or data[i] != data[i - 1]:
            answer += data[i]

    print(answer)