import sys

input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]


# 병합 정렬 함수
def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        index1, index2 = low, mid

        while index1 < mid and index2 < high:
            if arr[index1] < arr[index2]:
                temp.append(arr[index1])
                index1 += 1
            else:
                temp.append(arr[index2])
                index2 += 1

        while index1 < mid:
            temp.append(arr[index1])
            index1 += 1
        while index2 < high:
            temp.append(arr[index2])
            index2 += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, N)


merge_sort(numbers)
print(*numbers, sep="\n")
