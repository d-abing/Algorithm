import random

n = int(input())
set_menus_for_today = []
for _ in range(n):
    menus = input().split()
    set_menus_for_today.append(menus)

print(*(random.choice(set_menus_for_today)), sep="\n")
