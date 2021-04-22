import cv2
import numpy as np
import utils

path = "fotos/teste2.jpg"
width = 586
height = 826

widthG = 165
heightG = 805


img = cv2.imread(path) #Lendo a imagem
img = cv2.resize(img, (width, height)) #diminuindo a largura e altura da imagem
imgContours = img.copy()
imgBiggestContours = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
imgCanny = cv2.Canny(imgBlur, 10, 50)


countours, hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(imgContours, countours,-1,(0,255,0),5)


rectCon = utils.rectContour(countours)
biggestContour = utils.getCornerPoints(rectCon[0])
#print(biggestContour.shape)


if biggestContour.size != 0:
  cv2.drawContours(imgBiggestContours, biggestContour, -1, (0,255,0), 10)
  
  biggestContour = utils.reorder(biggestContour)
  
  pt1 = np.float32(biggestContour)
  pt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
  matrix = cv2.getPerspectiveTransform(pt1,pt2)
  imgWarpColored = cv2.warpPerspective(img,matrix,(width,height))
  
  imgWarpGray = cv2.cvtColor(imgWarpColored,cv2.COLOR_BGR2GRAY)
  imgThresh = cv2.threshold(imgWarpGray, 170, 255,cv2.THRESH_BINARY_INV )[1]
  
  #print(imgThresh)
  
  utils.splitBoxes(imgThresh)
  


imgBlack = np.zeros_like(img)
#[img,imgGray,imgBlur,imgCanny],
imgArray = ([imgContours,imgBiggestContours,imgWarpColored,imgBlack],
            [imgBlack,imgBlack,imgBlack,imgBlack])
imgStacked = utils.stackImages(imgArray, 0.5)

cv2.imshow("Stacked",imgStacked)

cv2.waitKey(0)
cv2.destroyAllWindows()