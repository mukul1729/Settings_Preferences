import math
number = 1000
prime = []
for a in range(0, number):
    prime.append(a)
    prime[a] = True
prime[0] = False
prime[1] = False
for a in range(2, int(math.sqrt(number))):
    if prime[a] == 1:
        for j in range(2, int(number / a)):
            prime[a * j] = 0

for a in range(0, number):
    if prime[a]:
        print(a)
