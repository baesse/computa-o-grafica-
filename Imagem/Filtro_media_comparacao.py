import cv2
import numpy as np

img = cv2.imread('arquivos/lena.png')
img = img[::3,::3]
imagem_filtrado = np.vstack([
 np.hstack([img, cv2.blur(img, ( 3, 3))]),
 np.hstack([cv2.blur(img, (5,5)), cv2.blur(img, ( 7, 7))]),
 np.hstack([cv2.blur(img, (9,9)), cv2.blur(img, (11, 11))]),
 ])
cv2.imshow("Imagens suavisadas", imagem_filtrado)
cv2.waitKey(0)
