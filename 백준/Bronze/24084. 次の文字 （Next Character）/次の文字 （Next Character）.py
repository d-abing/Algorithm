N = int(input())
S = input()
answer = ""

for i in range(N - 1):
    if S[i + 1] == "J":
        answer += S[i]

print(*answer, sep="\n")