from pwn import xor

c = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
C = bytes.fromhex(c)
for i in range(0,255,1):
    flag = xor(i,C)
    FLAG = flag.decode()
    if(FLAG[:7]=='crypto{'):
        print(FLAG)
        break