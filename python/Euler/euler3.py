import math


def prime(number):
    x = 0
    for i in range(2, int(math.sqrt(int(number) + 1))):
        if int(number) % i == 0:
            x = 1
    if x == 1:
        return(0)
    else:
        return(1)


n1 = int(input("Enter the number"))
set = []
for a in range(2, int(math.sqrt(int(n1) + 1))):
    if int(n1) % a == 0:
        if prime(a) == 1:
            set.append(a)
print(set)
max = set[0]
for i in range(len(set)):
    if set[i] > max:
        max = set[i]

print(max)
