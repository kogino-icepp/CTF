from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD
import base64
from Crypto.PublicKey import RSA
with open("privacy_enhanced_mail.pem",'r') as key_file:
    key = RSA.importKey(key_file.read())
    flag = key.d
    print(flag)
