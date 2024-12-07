import cv2

#Capturando uma imagem 
imagem = cv2.imread("pessoas.jpg")

cv2.imshow("pessoas", imagem)

#Carregar caracteristicas do arquivo
cascadFace = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Converter a imagem para tons de cinza
imagemPretoBraco = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

#Verificar se a imagem esta preta e branca
cv2.imshow("imagemPretoBraco", imagemPretoBraco)

#Detectando rostos e desenhando um quadrado
faces = cascadFace.detectMultiScale(imagemPretoBraco, scaleFactor=1.3, minNeighbors=5, minSize=(30,30))

for (x, y, w, h) in faces:
    cv2.rectangle(imagem, (x,y), (x+w, y+h), (000, 255, 000), 2)
cv2.imshow("resultado",imagem)




cv2.waitKey(0)
cv2.destroyAllWindows()



































