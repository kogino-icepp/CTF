import cv2
import matplotlib.pyplot as plt


img1 = cv2.imread('lemur.png')
img2 = cv2.imread('flag.png')
bitwise_xor = cv2.bitwise_xor(img1,img2)
plt.imshow(bitwise_xor)
cv2.imwrite('final.png',bitwise_xor)