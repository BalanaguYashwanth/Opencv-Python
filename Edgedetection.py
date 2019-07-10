import cv2
import numpy as np


face_cascade = cv2.CascadeClassifier("C:\\Users\\Admin\\Downloads\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("C:\\Users\\Admin\\Downloads\\opencv\\sources\\data\\haarcascades\\haarcascade_eye.xml")


img = cv2.imread('mosquito1.jpg')
edges = cv2.Canny(img, 100, 200)

cv2.imshow("Edge Detected Image", edges)

cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image




