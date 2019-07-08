x = 0
arr = []
for a in range(100000000, 250000000):
    for div in range(1, 21):
        if a % div == 0:
            x = x + 1
        if x == 20:
            arr.append(a)
            break
    x = 0
print(arr)
