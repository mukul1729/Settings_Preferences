import math
sum1 = 0
for a in range(1000, 99999):
    d1 = math.floor(a / 10000)
    d2 = math.floor((a / 1000) % 10)
    d3 = math.floor((a / 100) % 10)
    d4 = math.floor(a / 10) % 10
    d5 = math.floor(a % 10)
    sum = math.pow(d1, 5) + math.pow(d2, 5) + math.pow(d3, 5) + \
        math.pow(d4, 5) + math.pow(d5, 5)
    if a == sum:
        sum1 = sum1 + a
        print(sum1)
