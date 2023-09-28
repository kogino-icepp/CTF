from Crypto.PublicKey import RSA
with open('bruce_rsa.pub',"rb") as f:
    public_key =f.read()
public_data = RSA.importKey(public_key)
print(public_data.n)