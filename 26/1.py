import cv2
import numpy as np

chess_board = np.zeros((600,600))
for i in range(0,600,75):
    for j in range(0,600,75):
        if (np.mod(j,2)==0 and np.mod(i,2)==0) or (np.mod(j,2)!=0 and np.mod(i,2)!=0):
            chess_board[i:i+75,j:j+75] = 255

cv2.imshow('chess board',chess_board)
cv2.waitKey()
cv2.imwrite('Output/ChessBoard.jpg',chess_board)