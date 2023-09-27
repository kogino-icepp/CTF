from pwn import xor
k1 = 'label'
k2 = 13
ans = xor(k1,k2)
print('crypto{{{}}}'.format(ans))