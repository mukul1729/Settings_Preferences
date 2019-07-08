match = 0
for a in range(200, 500):
    for b in range(200, 500):
        for c in range(200, 500):
            match = (a * a + b * b) - (c * c)
            if match == 0:
                if a + b + c == 1000:
                    print(a * b * c)
