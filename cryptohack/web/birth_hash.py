n = 1 << 11

for i in range(1,10000000):
    P = pow((n-1)/n,i)
    if P<0.25:
        print(i)
        break