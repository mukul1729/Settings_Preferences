power = 1
for a in range(1, 1001):
    power *= 2
print(power)
number = 0
num = power
while num > 0:
    number += (int)(num % 10)
    num /= 10
print(number)
