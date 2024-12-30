S = input()
current = 0
i = 0
answer = S[current]

while current < len(S) - 1:
    i = ord(S[current]) - ord("A") + 1
    current += i
    answer += S[current]

print(answer)
