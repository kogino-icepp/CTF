import math
from fractions import Fraction
from Crypto.Util.number import *
class ContinuedFraction:
    def __init__(self, q: list):
        # m >= 1において、q_m >= 2を満たすため。
        if len(q) != 1 and q[-1] == 1:
            q = q[:-1]
            q[-1] += 1
            
        self._q = q
        self._nest = len(q) - 1
    
    @property
    def q(self):
        return self._q
    
    @property
    def nest(self):
        return self._nest
    
    def __str__(self):
        output_list = ["<"]
        for q_i in self.q:
            output_list.append(str(q_i))
            output_list.append(",")
        output_list[-1] = ">"
        return "".join(output_list)


def inv(f: Fraction):
    return Fraction(f.denominator, f.numerator)


def fraction_to_continued(f: Fraction):
    q_0 = math.floor(f)
    q = [q_0]
    previous_r_i = f - q_0
    
    while previous_r_i != 0:
        inv_previous_r_i = inv(previous_r_i)
        q_i = math.floor(inv_previous_r_i)
        previous_r_i = inv_previous_r_i - q_i
        
        q.append(q_i)
    
    return ContinuedFraction(q)

def continued_to_fraction(f: ContinuedFraction):
    q = f.q
    nest = f.nest
    
    n_0 = q[0]
    d_0 = 1
    if nest == 0:
        return Fraction(n_0, d_0)
    
    n_1 = q[0] * q[1] + 1
    d_1 = q[1]
    if nest == 1:
        return Fraction(n_1, d_1)
    
    n_i_minus_2 = n_0
    n_i_minus_1 = n_1
    d_i_minus_2 = d_0
    d_i_minus_1 = d_1
    
    n_i = None
    d_i = None
    
    # nest=len(q) - 1であるため
    for i in range(2, nest+1):
        n_i = q[i]*n_i_minus_1 + n_i_minus_2
        d_i = q[i]*d_i_minus_1 + d_i_minus_2
        
        n_i_minus_2, n_i_minus_1 = n_i_minus_1, n_i
        d_i_minus_2, d_i_minus_1 = d_i_minus_1, d_i
    
    return Fraction(n_i, d_i)


def calc_p_q_orelse(k, dg, e, n):
    if (e*dg) % k == 0:
        return -1, -1
    
    phi = e*dg // k
    
    if (n - phi + 1) % 2 != 0:
        return -1, -1
    
    X = (n - phi + 1) // 2
    Y2 = X*X - n
    
    if Y2 < 0:
        return -1, -1
    
    Y = math.isqrt(Y2)
    
    if Y*Y != Y2:
        return -1, -1
    
    return X+Y, X-Y



def wieners_attack(e, n):
    f_prime = Fraction(e, n)
    f_prime_continued = fraction_to_continued(f_prime)
    
    for i in range(f_prime_continued.nest+1):
        new_q = f_prime_continued.q[:i+1]
        if i % 2 == 0:
            new_q[-1] += 1
        new_continued_fraction = ContinuedFraction(new_q)
        new_fraction = continued_to_fraction(new_continued_fraction)
        k = new_fraction.numerator
        dg = new_fraction.denominator
        
        p, q = calc_p_q_orelse(k, dg, e, n)
        if p != -1 and q != -1:
            return p, q
    
    return -1, -1



n = 0xb8af3d3afb893a602de4afe2a29d7615075d1e570f8bad8ebbe9b5b9076594cf06b6e7b30905b6420e950043380ea746f0a14dae34469aa723e946e484a58bcd92d1039105871ffd63ffe64534b7d7f8d84b4a569723f7a833e6daf5e182d658655f739a4e37bd9f4a44aff6ca0255cda5313c3048f56eed5b21dc8d88bf5a8f8379eac83d8523e484fa6ae8dbcb239e65d3777829a6903d779cd2498b255fcf275e5f49471f35992435ee7cade98c8e82a8beb5ce1749349caa16759afc4e799edb12d299374d748a9e3c82e1cc983cdf9daec0a2739dadcc0982c1e7e492139cbff18c5d44529407edfd8e75743d2f51ce2b58573fea6fbd4fe25154b9964d
e = 0x9ab58dbc8049b574c361573955f08ea69f97ecf37400f9626d8f5ac55ca087165ce5e1f459ef6fa5f158cc8e75cb400a7473e89dd38922ead221b33bc33d6d716fb0e4e127b0fc18a197daf856a7062b49fba7a86e3a138956af04f481b7a7d481994aeebc2672e500f3f6d8c581268c2cfad4845158f79c2ef28f242f4fa8f6e573b8723a752d96169c9d885ada59cdeb6dbe932de86a019a7e8fc8aeb07748cfb272bd36d94fe83351252187c2e0bc58bb7a0a0af154b63397e6c68af4314601e29b07caed301b6831cf34caa579eb42a8c8bf69898d04b495174b5d7de0f20cf2b8fc55ed35c6ad157d3e7009f16d6b61786ee40583850e67af13e9d25be3
c = 0x3f984ff5244f1836ed69361f29905ca1ae6b3dcf249133c398d7762f5e277919174694293989144c9d25e940d2f66058b2289c75d1b8d0729f9a7c4564404a5fd4313675f85f31b47156068878e236c5635156b0fa21e24346c2041ae42423078577a1413f41375a4d49296ab17910ae214b45155c4570f95ca874ccae9fa80433a1ab453cbb28d780c2f1f4dc7071c93aff3924d76c5b4068a0371dff82531313f281a8acadaa2bd5078d3ddcefcb981f37ff9b8b14c7d9bf1accffe7857160982a2c7d9ee01d3e82265eec9c7401ecc7f02581fd0d912684f42d1b71df87a1ca51515aab4e58fab4da96e154ea6cdfb573a71d81b2ea4a080a1066e1bc3474
p, q = wieners_attack(e, n)
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
print(f"p: {p}")
print(f"q: {q}")
print(long_to_bytes(pow(c, d, n)).decode())
