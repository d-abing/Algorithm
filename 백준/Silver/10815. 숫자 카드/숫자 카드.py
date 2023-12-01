import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
numbers = list(map(int, input().split()))


def binary_search(target):
    has_found = False
    start = 0
    end = N - 1
    while start <= end:
        middle = (end + start) // 2
        if target < cards[middle]:
            end = middle - 1
        elif target > cards[middle]:
            start = middle + 1
        else:
            has_found = True
            break

    return has_found


for num in numbers:
    if binary_search(num):
        print(1, end=' ')
    else:
        print(0, end=' ')
