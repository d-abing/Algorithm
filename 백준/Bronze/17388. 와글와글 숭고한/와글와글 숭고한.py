S, K, H = map(int, input().split())
if S + K + H >= 100:
    print("OK")
else:
    min_score = min(S, K, H)
    if S == min_score:
        print("Soongsil")
    elif K == min_score:
        print("Korea")
    elif H == min_score:
        print("Hanyang")
    