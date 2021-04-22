import numpy as np
import cv2

def rgb2hsv(r, g, b):
  r, g, b = r/255.0, g/255.0, b/255.0
  mx = max(r, g, b)
  mn = min(r, g, b)
  df = mx-mn
  if mx == mn:
    h = 0
  elif mx == r:
    h = (60 * ((g-b)/df) + 360) % 360
  elif mx == g:
    h = (60 * ((b-r)/df) + 120) % 360
  elif mx == b:
    h = (60 * ((r-g)/df) + 240) % 360
  if mx == 0:
    s = 0
  else:
    s = df/mx*100
  v = mx*100
  return h, s, v 

cap = cv2.imread('fotos/cartao_01.jpg', 0)

def matrix(mat,token, pos):
  mtx = mat

  row = int(pos/4)
  col = pos%4
  
  for i in range(row+1): 
    if(row==len(mtx)):
      mtx.append([])
    for j in range(col+1):
      if(i==row and j==col):
        mtx[row].append(token)
  return mtx
# ccap = cv2.cvtColor(cap, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(
    cap,
    cv2.HOUGH_GRADIENT,
    1,
    20,
    param1=50,
    param2=30,
    minRadius=10,
    maxRadius=30
    )
array = []
circles = np.uint16(np.around(circles))
cap = cv2.imread('fotos/cartao_01.jpg')
cont = 0
mtx = []
for i in circles[0, :]:
  cont = cont + 1
  cv2.circle(cap, (i[0], i[1]), i[2], (0, 255, 0), 2)
  x = i[0]
  y = i[1]
  Red = cap[i[1], i[0], [2]]
  Green = cap[i[1], i[0], [1]]
  Blue = cap[i[1], i[0], [0]]
  
  if(int(Red)==0 and int(Green)==0 and int(Blue)==0):
    cv2.circle(cap, (i[0], i[1]), i[2], (255, 0, 0), 3)
    token="B"
    array.append(True)
  else: 
    token="W"
    array.append(False)
  mtx = matrix(mtx,token,cont-1)
  # cv2.putText(cap,str(cont), (x-10, y+5), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 255))
  cv2.putText(cap,token + "," + str(cont), (x-10,y+5), cv2.FONT_HERSHEY_SIMPLEX, .35, (0, 0, 255))
cv2.imshow('detect circles', cap)

print(circles.shape[1])
print(array)
cv2.waitKey(0)
cv2.destroyAllWindows()

