def fibonnaci():
    terms = [1,2]
    n = 0
    sum = 0
    while terms[n+1] < 4000000:
        terms.append(terms[n]+terms[n+1])
        n += 1
    for num in terms:
        if num % 2 == 0:
            sum += num 
    return sum

print fibonnaci()

# Should work but takes too long

def p0002_fast(n):
    a, b = 0, 1
    while True:
        if a > n:
            return
        yield a
        a, b = b, a + b
    fb = p0002_fast(4000000)
    total = 0 
    for x in fb:
        if (x%2 == 0):
            total += x
    print(total)

