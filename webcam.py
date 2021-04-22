import cv2

face_cascade = cv2.CascadeClassifier('haarcascades\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascades\haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)


while(1):
  ret, img = cap.read()
  img = cv2.flip(img,1)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(
    gray, 
    scaleFactor=1.2, 
    minNeighbors=5, 
    minSize=(20,20)
  )

  for(x, y, l, a) in faces:
    cv2.rectangle(img, (x, y), (x + l, y + a), (0,255,0), 2)
    roi_gray = gray[y:y+a, x:x+l]
    roi_color = img[y:y+a, x:x+l]
    
    eyes = eye_cascade.detectMultiScale(
      roi_gray,
      scaleFactor= 1.5,
      minNeighbors=5,
      minSize=(5, 5),
    )

    for (ex,ey,el,ea) in eyes:
      cv2.rectangle(roi_color, (ex, ey), (ex + el, ey + ea), (255,0,0), 2)
  
  cv2.imshow('video', img)
  print(faces)
  k = cv2.waitKey(30) & 0xFF
  if k == 27:
    break
cap.release()
cv2.destroyAllWindows() 