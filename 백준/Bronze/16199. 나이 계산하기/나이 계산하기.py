birthday = list(map(int, input().split()))
baseday = list(map(int, input().split()))

basic_age = baseday[0] - birthday[0] - 1
if baseday[1] > birthday[1] or (baseday[1] == birthday[1] and baseday[2] >= birthday[2]):
    basic_age += 1

year_age = baseday[0] - birthday[0]
korean_age = year_age + 1

print(basic_age)
print(korean_age)
print(year_age)
