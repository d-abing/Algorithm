for _ in range(3):
    sh, sm, ss, eh, em, es = map(int, input().split())
    H = eh - sh
    M = em - sm
    S = es - ss

    if S < 0:
        S += 60
        M -= 1

    if M < 0:
        M += 60
        H -= 1

    print(H, M, S)