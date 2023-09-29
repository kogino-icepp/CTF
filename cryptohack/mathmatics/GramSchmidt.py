import numpy as np

def gram_schmidt(vectors):
    basis = []
    basis.append(vectors[0].astype(float)) 
    for i in range(1, 4, 1):
        v = vectors[i].astype(float)
        for u in basis:
            mu = np.dot(v, u) / np.dot(u, u)
            v -= mu * u
        basis.append(v)
    return basis

V = np.array([[4, 1, 3, -1], [2, 1, -3, 4], [1, 0, -2, 7], [6, 2, 9, -5]])
result = gram_schmidt(V)
for b in result:
    print(b)
