import cv2
import numpy as np
vidcap = cv2.VideoCapture('./arquivos/mov_bbb.mp4')
success,image = vidcap.read()
count = 0
height , width , layers =  image.shape
video = cv2.VideoWriter('video_media.avi',0,60,(width,height)) 
video2 = cv2.VideoWriter('video_mediana.avi',0,60,(width,height)) 
while success:
    img_filtro_media = cv2.blur(image, ( 5, 5))
    video.write(img_filtro_media)    
    imagem_filtrada2 = np.vstack([
    np.hstack([image,cv2.medianBlur(image, 3)])])
    video2.write(imagem_filtrada2)
    success,image = vidcap.read() 
cv2.destroyAllWindows()
video.release()
vidcap.release()
video2.release()