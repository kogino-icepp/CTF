def gcd(a, b):
    r = a % b

    while r != 0:
        a, b = b, r
        r = a % b

    return b
a = 66528
b = 52920

print(gcd(a,b))