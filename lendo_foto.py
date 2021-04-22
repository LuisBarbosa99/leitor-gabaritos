import numpy
import cv2

face_cascade = cv2.CascadeClassifier('haarcascades\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascades\haarcascade_eye.xml')

imagem = cv2.imread('fotos/1.jpg')

cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(cinza, scaleFactor=1.05, minNeighbors=2, minSize=(30,30))

print(faces)

for(x, y, l, a) in faces:
  cv2.rectangle(imagem, (x, y), (x + l, y + a), (0,255,0), 2)
  roi_gray = cinza[y:y+a, x:x+l]
  roi_color = imagem[y:y+a, x:x+l]
  eyes = eye_cascade.detectMultiScale(roi_gray)
  for (ex,ey,el,ea) in eyes:
    cv2.rectangle(roi_color, (ex, ey), (ex + el, ey + ea), (255,0,0), 2)
cv2.imshow("Faces", imagem)
cv2.waitKey()