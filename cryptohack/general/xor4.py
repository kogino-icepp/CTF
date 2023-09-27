from pwn import xor
c = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
C = bytes.fromhex(c)
test_key = 'crypto{'
cand_key = 'myXORkey'
#test_flag = xor(C,test_key.encode())
#print(test_flag.decode())
cand_flag = xor(C,cand_key.encode())
print(cand_flag.decode())