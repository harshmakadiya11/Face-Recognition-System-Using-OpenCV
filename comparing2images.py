import sys 
import cv2
import numpy as np 
import face_recognition
import pandas as pd 

img1=input("enter tthe image one")
image1=cv2.imread(img1)
if(image1 is not None):
    cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
#rbg_img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img_location=face_recognition.face_locations(image1)[0]
img_encoding1 = face_recognition.face_encodings(image1)[0]
cv2.rectangle(image1,(img_location[3],img_location[0]),(img_location[1],img_location[2]),(255,0,255),2)
cv2.imshow("IMAGE1",image1)
key = cv2.waitKey(0)
if key == ord('x'):
    cv2.destroyAllWindows()
img2=input("enter second image  ")
image2=cv2.imread(img2)

#rbg_img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
if(image2 is not None):
    cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
img2_location=face_recognition.face_locations(image2)[0]    
img_econding2=face_recognition.face_encodings(image2)[0]
cv2.rectangle(image2,(img2_location[3],img2_location[0]),(img2_location[1],img2_location[2]),(255,0,255),2)
cv2.imshow("IMAGE2",image2)
cv2.waitKey(0)


reuslt=face_recognition.compare_faces(img_encoding1,[img_econding2])
print('result=',reuslt)

