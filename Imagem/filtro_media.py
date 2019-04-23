import cv2
#Leitura da Imagem
img = cv2.imread('arquivos/lena.png')

img_filtro_media = cv2.blur(img, ( 5, 5))
cv2.imshow("Imagens Filtrada", img_filtro_media)
cv2.waitKey(0)
