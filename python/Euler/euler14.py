series = []
for num in range(500000, 1000000):
    series.append(num)
    x = num
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = (3 * num) + 1
        series.append(num)

    print(len(series), x)
    series.clear()
