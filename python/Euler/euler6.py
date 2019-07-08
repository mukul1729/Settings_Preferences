square_sum = 0
sum = 0
for a in range(1, 101):
    sum = sum + a * a
for a in range(1, 101):
    square_sum = square_sum + a
square_sum *= square_sum
print(square_sum - sum)
