import cv2 , pandas
from datetime import datetime

#face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video = cv2.VideoCapture(0)
first_frame = None
status_list = [None,None]
times = []
df = pandas.DataFrame(columns=['Start','End'])

while True:
    check, frame = video.read()
    status = 0
    
    grey_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    grey_img = cv2.GaussianBlur(grey_img,(21,21),0)

    if first_frame is None :
        first_frame = grey_img
        continue
    
    Delta_Frame = cv2.absdiff(first_frame,grey_img)
    Threshold = cv2.threshold(Delta_Frame,30 ,255 ,cv2.THRESH_BINARY)[1]
    Threshold = cv2.dilate(Threshold,None, iterations= 2)

    (cnts,_) = cv2.findContours(Threshold.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        status = 1
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    status_list.append(status)

    status_list = status_list[-2:]
     
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    cv2.imshow("Grey Image",grey_img)
    cv2.imshow("Delta Frame",Delta_Frame)
    cv2.imshow("ThreShold Frame",Threshold)
    cv2.imshow("Color Image",frame)
    #print(grey_img)
    #print(status)

    key=cv2.waitKey(1)
    if key == ord('q'):
        if status == 1:
            times.append(datetime.now()) 
        break

for i in range(0,len(times),2):
    df= df.append({'Start':times[i],'End':times[i+1]},ignore_index= True)

df.to_csv("times.csv")

print(status_list)
print(times)

cv2.destroyAllWindows()