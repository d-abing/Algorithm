while True:
    N = float(input())
    if N < 0:
        break

    X = format(N, ".2f")
    Y = format(N * 0.167, ".2f")

    print("Objects weighing {} on Earth will weigh {} on the moon.".format(X, Y))