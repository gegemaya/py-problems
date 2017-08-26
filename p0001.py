def problem():
    sum = 0
    for x in range(1000):
        if x % 3 == 0 or x % 5 == 0:
            sum += x
    return sum

print problem()



def p0001_fast(a,b,n):
    len_a = (n-1)/a
    len_b = (n-1)/b
    len_ab = (n-1)/(a*b)

    sum_a = a * len_a * (len_a + 1) / 2
    sum_b = b * len_b * (len_b + 1) / 2
    sum_ab = a * b * len_ab * (len_ab +1) / 2

    sum_n = sum_a +sum_b - sum_ab

    return sum_n

print p0001_fast(3, 5, 1000)
