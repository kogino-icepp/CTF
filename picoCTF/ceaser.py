def CC_encryption( text, key ):
     result = ''
     for char in list(text):      
          code = ord(char)
          if 97 <= code and code <= 122:  #小文字の場合
              n = code - 97
              n = (n + key) % 26
              code = n + 97
              result += chr(code)
          elif 65 <= code and code <= 90:  #大文字の場合
              n = code - 65
              n = (n + key) % 26
              code = n + 65
              result += chr(code)
          else:
               result+= chr(code) 
     return result

encrypt_text = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_Ncualgvd}"
for i in range(0,26):
     print("key"+str(i)+": "+CC_encryption(encrypt_text,i))