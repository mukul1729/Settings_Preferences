def palindrome(number):
    pal = 0
    n = number
    while number > 0:
        mod = number % 10
        number = int(number / 10)
        pal = pal * 10 + mod
    if(pal == n):
        return(1)
    else:
        return(0)


mul = 1
arr = []
for a in range(100, 1000):
    for p in range(100, 1000):
        mul = a * p
        if palindrome(mul) == 1:
            arr.append(mul)
lar = arr[0]
for largest in range(int(len(arr))):
    if arr[largest] > lar:
        lar = arr[largest]

print(lar)
