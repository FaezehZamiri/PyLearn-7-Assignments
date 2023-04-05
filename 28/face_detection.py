import cv2
import numpy as np

cap = cv2.VideoCapture(0)
img = cv2.imread('Input/person.jpg')
img_sticker = cv2.imread('Input/emoji.jpg')
img_sticker2 = cv2.imread('Input/lips.jpg')

def chess_face(faces,frame):
    for face in faces:
        x,y,w,h = face
        face_image = frame[y:y+h,x:x+w] 
        face_image_small = cv2.resize(face_image,[15,15])
        face_image_big = cv2.resize(face_image_small,[w,h],interpolation = cv2.INTER_NEAREST)
        frame[y:y+h,x:x+w] = face_image_big
    
    return frame

def sticker_face(faces,frame):
    for face in faces:
        x,y,w,h = face
        sticker = cv2.resize(img_sticker,[w,h])
        for i in range(h):
            for j in range(w):
                if sticker[i][j][0] == 201 and sticker[i][j][1] == 174 and sticker[i][j][2] == 255:
                    sticker[i][j] = frame[y+i,x+j]
        frame[y:y+h,x:x+w] = sticker

    return frame

def sticker_lip_eye(frame,frame_gray):
    smile_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
    smiles = smile_detector.detectMultiScale(frame_gray,1.1,8,minSize=(70, 75),maxSize=(130, 135))

    eye_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    eyes = eye_detector.detectMultiScale(frame_gray,1.3,minSize=(50, 50),maxSize=(150, 150))

    for smile in smiles:
            x,y,w,h = smile
            sticker_smile = cv2.resize(img_sticker2,[w,h])
            for i in range(h):
                for j in range(w):
                    if sticker_smile[i][j][0] == 255 and sticker_smile[i][j][1] == 255 and sticker_smile[i][j][2] == 255:
                        sticker_smile[i][j] = frame[y+i,x+j]
            frame[y:y+h,x:x+w] = sticker_smile
    

    for eye in eyes:
        x,y,w,h = eye
        p1=x+w//2
        p2=y+h//2
        cv2.circle(frame,[p1,p2],h//2,0,5)

    return frame

while True:
    _,frame = cap.read()
    row,col,band = frame.shape
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
    faces = face_detector.detectMultiScale(frame_gray,1.3)

    cv2.imshow('Default',frame)
    
    if cv2.waitKey(25) & 0xFF == ord('1'):
        sticker_face_frame = sticker_face(faces,frame)
        cv2.imshow('Face Detection',sticker_face_frame)

    if cv2.waitKey(25) & 0xFF == ord('2'):
        sticker_frame = sticker_lip_eye(frame,frame_gray)
        cv2.imshow('Face Detection',sticker_frame)

    if cv2.waitKey(25) & 0xFF == ord('3'):
        chess_face_frame = chess_face(faces,frame)
        cv2.imshow('Face Detection',chess_face_frame)

    if cv2.waitKey(25) & 0xFF == ord('4'):
        framelr = np.fliplr(frame)
        frame[:,0:col//2] = frame[:,0:col//2]
        frame[:,col//2:] = framelr[:,col//2:]
        cv2.imshow('Face Detection',frame)


    if cv2.waitKey(25) & 0xFF == ord('q'):
        break







