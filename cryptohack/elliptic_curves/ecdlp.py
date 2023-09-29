import scalar
import hashlib
a = 497
b = 1768
P = 9739
#print(scalar.add_point(a,b,X,Y,P))
G = [1804,5368]
Qa = [815, 3190]
nb = 1829
#Qb = scalar.ScalarMult(a,b,G,nb,P)
key = scalar.ScalarMult(a,b,Qa,nb,P)
sha1 = hashlib.sha1()
sha1.update(str(key[0]).encode())
print(sha1.hexdigest())
