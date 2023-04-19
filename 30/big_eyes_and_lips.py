import cv2
import numpy as np
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel

img  = cv2.imread('input/1.jpg')

lip = [55, 56, 53, 59, 58, 61, 68, 67, 71, 63, 64, 52]
left_eye  = [39, 37, 33, 36, 35, 41, 40, 42]
right_eye = [95, 94, 96, 93, 91, 87, 90, 89]


def ZoomFace(img,element):
    fd = UltraLightFaceDetecion("weights/RFB-320.tflite",conf_threshold=0.88)
    fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")
    img = img.astype(np.float32)
    
    boxes, _ = fd.inference(img)
    for pred in fa.get_landmarks(img, boxes):
        #for i,p in enumerate(np.round(pred).astype(np.int)):
            #cv2.circle(img, tuple(p), 1, (125, 255, 125), 1, cv2.LINE_AA)
            #cv2.putText(img,str(i),tuple(p),cv2.FONT_HERSHEY_PLAIN,0.5,(255,0,0),1)

        landmarks = []
        for i in element:
            landmarks.append(pred[i])

        landmarks = np.array(landmarks , dtype = int)
        x, y, w, h = cv2.boundingRect(landmarks)

        mask = np.zeros(img.shape, dtype = np.float32)
        
        cv2.drawContours(mask,[landmarks],-1,(255,255,255),-1)

        mask = mask / 255
        result = img * mask
        result = result[y:y+h , x:x+w]
        result_big = cv2.resize(result,(0,0),fx = 1.7 , fy = 1.7)
        result_big = result_big.astype(np.uint8)

        row,col,_ = result_big.shape
        for i in range(row):
            for j in range(col):
                if result_big[i][j][0] == 0 and result_big[i][j][1] == 0 and result_big[i][j][2] == 0:
                    result_big[i][j] = img[y+i,x-col//5+j]

        return result_big , x , y 


Lips , x_1 , y_1 = ZoomFace(img,lip)
LeftEye , x_2 , y_2 = ZoomFace(img,left_eye)
RightEye , x_3 , y_3 = ZoomFace(img,right_eye)

row_1,col_1,_ = Lips.shape
img[y_1:y_1+row_1 , x_1-col_1//5:x_1+4*col_1//5] = Lips

row_2,col_2,_ = LeftEye.shape
img[y_2-5:y_2+row_2-5 , x_2-col_2//5:x_2+1+4*col_2//5] = LeftEye

row_3,col_3,_ = RightEye.shape
img[y_3-5:y_3+row_3-5 , x_3-col_3//5:x_3+1+4*col_3//5] = RightEye



cv2.imshow("", img)
cv2.imwrite('output/Big eyes and lips.jpg',img)
cv2.waitKey()
