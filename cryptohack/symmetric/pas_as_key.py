import requests
import random
import hashlib
from Crypto.Cipher import AES
import binascii

result = requests.get('http://aes.cryptohack.org/passwords_as_keys/encrypt_flag/')
ciphertext = result.json()["ciphertext"]
with open("/usr/share/dict/words") as f:
    #print(f)
    for words in f.readlines():
        words = words.strip()
        #ciphertext = bytes.fromhex(ciphertext)
        key = hashlib.md5(words.encode()).hexdigest()
        #key = bytes.fromhex(key)
        #print(key)
        m = requests.get(f'http://aes.cryptohack.org/passwords_as_keys/decrypt/{ciphertext}/{key}/')
        m = m.json()["plaintext"]
        
        
        

