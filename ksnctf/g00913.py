from mpmath import mp
mp.dps = 100

#\u7d20\u6570\u5224\u5b9a
def is_prime(n):
    if n == 1: return False

    for k in range(2, int(mpmath.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


str_pi=str(pi)

for i in range(2,mp.dps-10):
    if(is_prime(int(str_pi[i:i+10]))):
        print(str_pi[i:i+10])
        break

