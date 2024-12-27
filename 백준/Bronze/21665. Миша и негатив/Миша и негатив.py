n, m = map(int, input().split())
input_image = [input() for _ in range(n)]
input()
output_image = [input() for _ in range(n)]
count = 0

for i in range(n):
    for j in range(m):
        if input_image[i][j] == "W" and output_image[i][j] == "B":
            continue
        elif input_image[i][j] == "B" and output_image[i][j] == "W":
            continue
        else:
            count += 1

print(count)