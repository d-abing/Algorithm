X = int(input())
Y = int(input())

years = []

for year in range(X, Y + 1, 60):
    years.append(year)

for year in years:
    print("All positions change in year {}".format(year))