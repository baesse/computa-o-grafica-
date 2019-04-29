import cv2
import numpy as np
# Carregar o video para memória
vidcap = cv2.VideoCapture('./arquivos/mov_bbb.mp4')
# Ler a primeira imagem do video
success,image = vidcap.read()
count = 0
# capturar as dimensões do frame proveniente do video 
height , width , layers =  image.shape

# Criar os videos que receberam os frames editados
video = cv2.VideoWriter('video_media.avi',0,60,(width,height)) 
video2 = cv2.VideoWriter('video_mediana.avi',0,60,(width,height)) 

#Percorrer cada frame do video
while success:
    #Aplica o filtro no primeiro frame 
    img_filtro_media = cv2.blur(image, ( 5, 5))
     #escreve o frame no video novo 
    video.write(img_filtro_media)   

    #Aplica o filtro no primeiro frame 
    imagem_filtrada2 = np.vstack([
    np.hstack([image,cv2.medianBlur(image, 3)])])
    #escreve o frame no video novo  com hstack
    video2.write(imagem_filtrada2)
    #and para o próximo frame do video original 
    success,image = vidcap.read() 
cv2.destroyAllWindows()
#remove os videos da memora e escreve em disco
video.release()
vidcap.release()
video2.release()