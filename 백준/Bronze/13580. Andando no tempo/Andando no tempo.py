years = list(map(int, input().split()))

years.sort(reverse=True)
answer = "N"

if years[0] == sum(years[1:]):
    answer = "S"
    
for i in range(2):
    if years[i + 1:].count(years[i]):
        answer = "S"

print(answer)