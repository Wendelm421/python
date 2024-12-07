#Importar biblioteca Opencv
import cv2

#Utilizar o arquivo detector de rostos/faces
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Abir a camera
camera = cv2.VideoCapture(0)

while True:
    sucesso, frame = camera.read()
    #cv2.imshow("webcam", frame)
    #Converter a imagem para tons de cinza
    FramePretoBraco = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Verificar se a imagem esta preta e branca
    cv2.imshow("webcam", FramePretoBraco)
    
    #Detectar os rostos/faces no frame
    rostos = detector.detectMultiScale(FramePretoBraco,scaleFactor=1.1, minNeighbors=1, minSize=(100,100))
    
    for (x, y, lar, alt) in rostos:
     cv2.rectangle(frame, (x,y), (x+lar, y+alt), (000, 255, 255), 2)
    #Exibindo o frame desenhado
    cv2.imshow("Rostos Detectados", frame)
    


    
    if cv2.waitKey(1) & 0xff == ord("s"):
        break




#Fecha streaming
camera.release()
cv2.destroyAllWindows()

































