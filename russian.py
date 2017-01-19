# naive function with deficient time range
# time: 3 + 2 * n
def naive(a, b):
    x = a
    y = b
    z = 0

    while x > 0:
        z = z + y
        x = x - 1

    return z

# russian functin is awesome
# time: <= 4 * (log2 a) + 7
def russian(a, b):
    x = a
    y = b
    z = 0

    while x > 0:
        if x % 2 == 1: z = z + y
        y = y << 1
        x = x >> 1

    return z

print russian(2**1000, 2**1000)
