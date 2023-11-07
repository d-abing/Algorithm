A = int(input())
B = int(input())
C = int(input())

num = [0] * 10

for s in str(A * B * C):
    num[int(s)] += 1

print(*num, sep="\n")
