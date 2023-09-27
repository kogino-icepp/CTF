from pwn import xor

key1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
KEY1 = bytes.fromhex(key1)
key12 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
KEY12 = bytes.fromhex(key12)
key23 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
KEY23 = bytes.fromhex(key23)
flag123= '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'
FLAG123 = bytes.fromhex(flag123)

KEY2 = xor(KEY1, KEY12)
KEY3 = xor(KEY2, KEY23)
FLAG = xor(FLAG123, KEY1, KEY2, KEY3)

flag = FLAG.decode()
print(flag)
