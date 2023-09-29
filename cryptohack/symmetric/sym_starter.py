import requests

result = requests.get('https://aes.cryptohack.org/block_cipher_starter/encrypt_flag')
ciphertext = result.json()["ciphertext"]
print(ciphertext)
M = requests.get(f'https://aes.cryptohack.org/block_cipher_starter/decrypt/{ciphertext}')
m = M.json()["plaintext"]
print(bytes.fromhex(m))