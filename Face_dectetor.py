from cgitb import grey
from ctypes import resize
import cv2
face_casacade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("Raja Ragavan.jpg")
grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_casacade.detectMultiScale(grey_img,
scaleFactor = 1.1,
minNeighbors = 5)

for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    #break

resized = cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))

print(type(faces))
print(faces[0])

cv2.imshow("Raja",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()