from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import scalar

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

#P=3(mod4)を想定
def GetY(a,b,x,P):
    y2 = x**3+a*x+b
    y = pow(-y2,(P+1)//4,P)
    return y
a = 497
b = 1768
P = 9739
G = [1804,5368]
nB = 6534
q_x = 4726
q_y = GetY(a,b,q_x,P)
print(q_y)
A = [q_x,q_y] 


shared_secret = scalar.ScalarMult(a,b,A,nB,P)
print(shared_secret[0])
iv = 'cd9da9f1c60925922377ea952afc212c'
ciphertext = 'febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8'
print(decrypt_flag(shared_secret[0], iv, ciphertext))
