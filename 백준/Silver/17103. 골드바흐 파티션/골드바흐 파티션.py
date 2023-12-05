import sys
input = sys.stdin.readline

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False

    return [x for x in range(limit + 1) if is_prime[x]]

primes = sieve_of_eratosthenes(1_000_000)

def count_prime_pairs(N):
    count = 0
    start, end = 0, len(primes) - 1

    while start <= end:
        current_sum = primes[start] + primes[end]
        if current_sum == N:
            count += 1
            start += 1
            end -= 1
        elif current_sum < N:
            start += 1
        else:
            end -= 1

    return count

T = int(input())
for _ in range(T):
    N = int(input())
    count = count_prime_pairs(N)
    print(count)
