import cv2
import pandas as pd 
from detection_of_image import detection 

#encodings of the konwn images 
det=detection()
det.load_encoding_images("D:\college\sem2\midterm\codes\known images")

camera=cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    #detect the faces
    face_locations , face_names = det.detect_known_faces(frame)
    for face_loc ,name in zip(face_locations,face_names):
        y1, x2, y2, x1= face_loc[0], face_loc[1], face_loc[2], face_loc[3]


        cv2.putText(frame, name,(x1,y1-10),cv2.FONT_HERSHEY_DUPLEX , 1 ,( 0 , 0 , 200 ) , 2 )
        cv2.rectangle(frame,(x1, y1), (x2, y2),(0,0,200),2)

    cv2.imshow("Frame",frame)

    key=cv2.waitKey(1)
    if key == 27:
        break
     
camera.release()
cv2.destroyAllWindows(2)










