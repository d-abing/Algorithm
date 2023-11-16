N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))[:-1]
minimum_price = price[0]
total_price = 0

for i in range(len(price)):
    if price[i] <= minimum_price:
        minimum_price = price[i]
    total_price += minimum_price * distance[i]

print(total_price)
