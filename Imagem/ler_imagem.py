import cv2
#Leitura da Imagem
img = cv2.imread('arquivos/lena.png')
#Apresenta uma imagem
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Transforma uma imagem em escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Apresenta a imagem em Escala de Cinza
cv2.imshow('imagem',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Salva a imagem transformada
cv2.imwrite('arquivos/lena_cinza.jpg',gray)

