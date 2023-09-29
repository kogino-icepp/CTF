from Crypto.Util.number import long_to_bytes
import gmpy2
from itertools import combinations
def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def inverse_modulo(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
def decrypt(grps, e):
    for grp in combinations(zip(grps['n'], grps['c']), e):
        N = 1
        for x in grp:
            N *= x[0]

        M = 0
        for x in grp:
            M += x[1]*inverse_modulo(N//x[0], x[0])*(N//x[0])
        M %= N

        m, exact = gmpy2.iroot(M, 3)
        if exact:
            print(long_to_bytes(m))


file = open("output.txt", 'rb')
e = 3
n = []
c = []
while True:
    data = file.readline()
    if data:
        if data[0] == 110:
            n.append(int(data.decode()[4:-1], 10))
        elif data[0] == 99:
            c.append(int(data.decode()[4:-1], 10))
    else:
        print("end")
        break
file.close()
groups = {'n': n, 'c': c}
print(decrypt(groups, e))