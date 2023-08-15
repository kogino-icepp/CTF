#strInputText
#intKey

def caesar(strInputText, intKey):
    strResultList = []
    for char in strInputText:
        if(ord(char)+intKey) <= ord('z'):
            strResultList.append(chr(ord(char)+ intKey))
        else:
            strResultList.append(chr((ord('a')-1)+(ord(char)+intKey-ord('z'))))

    print('key:'+str(intKey) + '>'+"".join(strResultList))

if __name__ == '__main__':
    for i in range(1,26):
        caesar('fsdz{Fdhvdu_flskhu_lv_fodvvlfdo_flskhu}',i)