import cv2

img = cv2.imread('Input/cats.jpeg')
img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

cat_face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')
cats = cat_face_detector.detectMultiScale(img_gray,1.3,1)

for face in cats:
        x,y,w,h = face
        cv2.rectangle(img,[x,y],[x+w,y+h],0,6)

print('Number of Cats: ',len(cats))
cv2.imwrite('Output/Cats.jpg',img)
cv2.imshow('',img)
cv2.waitKey()

