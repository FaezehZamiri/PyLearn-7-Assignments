import cv2
import numpy as np
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel

img = cv2.imread('input/2.jpg')
img = cv2.rotate(img,cv2.ROTATE_180)

img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

lip = [55, 56, 53, 59, 58, 61, 68, 67, 71, 63, 64, 52]
left_eye  = [ 37, 33, 36, 35, 41, 40, 42]
right_eye = [95, 94, 96, 93, 91, 87, 90, 89]

def RotateFace(img,element):
    fd = UltraLightFaceDetecion("weights/RFB-320.tflite",conf_threshold=0.6)
    fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")
    
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
        result = result.astype(np.uint8)

        row,col,_ = result.shape
        for i in range(row):
            for j in range(col):
                if result[i][j][0] == 0 and result[i][j][1] == 0 and result[i][j][2] == 0:
                    result[i][j] = img[y+i,x+j]

        result = cv2.rotate(result,cv2.ROTATE_180)
        result = np.fliplr(result)

        return result , x , y


Lips , x , y = RotateFace(img,lip) 
row_1,col_1,_ = Lips.shape
img[y:y+row_1 , x:x+col_1] = Lips

Right_eye , x3 , y3 = RotateFace(img,right_eye) 
row_3,col_3,_ = Right_eye.shape
img[y3:y3+row_3 , x3:x3+col_3] = Right_eye   

Left_eye , x2 , y2 = RotateFace(img,left_eye) 
Right_eye = np.fliplr(Right_eye)
row_2,col_2,_ = Right_eye.shape
img[y2:y2+row_2 , x2:x2+col_2] = Right_eye



cv2.imshow("", img)
cv2.imwrite('output/Rotate.jpg',img)
cv2.waitKey()

