def isin(a,b,p,P):
    if p == 0:
        return True
    x,y = p[0],p[1]
    value = y**2-x**3-a*x-b
    if value%P == 0:
        return True
    return False
def add_point(a,b,p,q,P):
    if not isin(a,b,p,P):
        return ValueError("{} is not in the curve".format(p))
    if not isin(a,b,q,P):
        return ValueError("{} is not in the curve".format(q))
    
    if p == 0:
        return q
    if q == 0:
        return p
    x1,y1,x2,y2 = p[0],p[1],q[0],q[1]
    if x1 == x2 and y1 == -y2:
        return 0
    lamb = 0
    if p!=q:
        lamb = (y2-y1)*pow((x2-x1),-1,P)
    else:
        lamb = (3*x1**2+a)*pow((2*y1),-1,P)
    x3 = lamb**2-x1-x2
    y3 = lamb*(x1-x3)-y1
    x3 %= P
    y3 %= P
    return [x3,y3]
def ScalarMult(a,b,p,n,P):
    if not isin(a,b,p,P):
        return ValueError("{} is not in the curve".format(p))
    q = p
    r = 0
    while n>0:
        if n%2==1:
            r = add_point(a,b,r,q,P)
        q = add_point(a,b,q,q,P)
        n = n//2
    return r

a = 497
b = 1768
P = 9739
p = [2339,2213]
n = 7863
#print(ScalarMult(a,b,p,n,P))