import math
tri_sum = 0
div = 0
for a in range(1, 2000):
    for j in range(1, a + 1):
        tri_sum = j + tri_sum
    for a in range(1, int(math.sqrt(tri_sum)) + 1):
        if tri_sum % a == 0:
            div += 2
    print(div)
    div = 0
    tri_sum = 0
