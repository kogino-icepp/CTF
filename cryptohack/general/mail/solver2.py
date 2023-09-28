from Crypto.PublicKey import RSA

# Import the RSA key from a file
with open('2048b-rsa.der', 'rb') as f:
    public_key_der = f.read()

public_key = RSA.import_key(public_key_der)
print(public_key.n)