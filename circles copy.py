import numpy as np
import cv2

path = 'fotos/cartao_01.jpg'

def rectContour(contours):
  
    rectCon = []
    max_area = 0
    for i in contours:
        area = cv2.contourArea(i)
        print("Area",area)
    #     if area >= 50:
    #         peri = cv2.arcLength(i, True)
    #         approx = cv2.approxPolyDP(i, 0.02 * peri, True)
    #         print("Corner Points",len(approx))
    #         if len(approx) == 4:
    #             rectCon.append(i)
    # rectCon = sorted(rectCon, key=cv2.contourArea,reverse=True)
    # return rectCon

img = cv2.imread(path)
imgContours = img.copy()
imgBiggestContours = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
imgCanny = cv2.Canny(imgBlur, 10, 50)

countours, hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(imgContours, countours,-1,(0,255,0),2)

rectContour(countours)
cv2.drawContours(imgBiggestContours, biggestContour, -1, (0,255,0), 10)
cv2.imshow("img", imgContours)

cv2.waitKey(0)
cv2.destroyAllWindows()
