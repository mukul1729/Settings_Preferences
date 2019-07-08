for i in range(2, 10000):
    x = 0
    for p in range(2, 10000):
        if i % p == 0:
            x = x + 1
    if x == 2:
        print(i)
