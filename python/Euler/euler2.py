first = 1
second = 1
third = 0
sum = 0
for a in range(100):
    third = first + second
    if third % 2 == 0 and sum <= 4000000:
        sum = sum + third
    first = second
    second = third
print(sum)
