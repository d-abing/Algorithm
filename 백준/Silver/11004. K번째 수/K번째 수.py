import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))


def quicksort(start, end, k):
    global A
    if start < end:
        pivot = partition(start, end)
        if pivot == k:
            return
        elif pivot < k:
            quicksort(pivot + 1, end, k)
        elif pivot > k:
            quicksort(start, pivot - 1, k)


def partition(start, end):
    global A

    if start + 1 == end:
        if A[start] > A[end]:
            A[start], A[end] = A[end], A[start]
        return end

    mid = (start + end) // 2
    A[start], A[mid] = A[mid], A[start]
    pivot = A[start]
    i = start + 1
    j = end

    while i <= j:
        while A[i] < pivot and i < len(A) - 1:
            i += 1
        while A[j] > pivot and j > 0:
            j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1

    if A[j + 1] < pivot:
        A[start], A[j + 1], A[j + 1], A[start]
    else:
        A[start], A[j] = A[j], A[start]
    return j


quicksort(0, N - 1, K - 1)
print(A[K - 1])
