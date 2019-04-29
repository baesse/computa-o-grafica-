import cv2
import numpy as np

img = cv2.imread('arquivos/lena.png')
img = img[::2,::2] # Diminui a imagem
imagem_filtrada = np.vstack([
 np.hstack([img,
 cv2.medianBlur(img, 3)]),
 np.hstack([cv2.medianBlur(img, 5),
 cv2.medianBlur(img, 7)]),
 np.hstack([cv2.medianBlur(img, 9),
 cv2.medianBlur(img, 11)]),
 ])
cv2.imshow("Imagem original e sua visadas pela mediana", imagem_filtrada)
cv2.waitKey(0)
