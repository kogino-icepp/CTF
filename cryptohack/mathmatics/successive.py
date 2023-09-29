import numpy as np
modu = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
    
for p in (852,1000,1):
    x = pow(modu[1]*modinv(modu[0],p),p)
    hantei = True
    for i in range(1,11,1):
        if x != pow(modu[i+1]*pow(modu[i],-1,p),p):
            hantei = False
            break
    if hantei:
        print(x,p)