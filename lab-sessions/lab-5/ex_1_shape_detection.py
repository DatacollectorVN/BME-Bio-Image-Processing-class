import cv2
import numpy as np
import argparse

def getContours(imgContour, imageCanny):
    contours, hierarchy = cv2.findContours(imageCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            cv2.drawContours(imgContour, cnt,-1,(255,0,0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri, True)
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            if objCor == 3: 
                objectType = "Tri"
            elif objCor == 4: 
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05: 
                    objectType = "Square"
                else: objectType = "Rectangle"
            elif objCor > 4: 
                objectType = "Circle"
            else: 
                objectType = "None"

            cv2.rectangle(imgContour, (x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(imgContour, objectType,(x+(w//2)-10,y+(h//2)- 10),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,255),2)

def main(image_file):
    img = cv2.imread(image_file)
    imgContour = img.copy()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7,7),1)
    imgCanny = cv2.Canny(imgBlur,50,50)
    getContours(imgContour, imgCanny)
    #imgStack = np.hstack((img,imgCanny))
    cv2.imshow('Image', img)
    cv2.imshow('Canny', imgCanny)
    cv2.imshow('Contoured', imgContour)
    cv2.waitKey(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--imagepath", dest = "image_file_path", type = str,
                        default = None, help = "Image file path")
    args = parser.parse_args()
    image_file_path = args.image_file_path
    main(image_file_path)
