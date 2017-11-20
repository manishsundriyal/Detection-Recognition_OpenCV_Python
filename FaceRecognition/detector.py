import cv2
import numpy as np
import sqlite3
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
def getProfile(id):
    conn=sqlite3.connect("FaceBase.db")
    cmd="SELECT * FROM People WHERE ID="+str(id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
        conn.close()
        return profile
    
cam=cv2.VideoCapture(0);
rec=cv2.face.createLBPHFaceRecognizer();
rec.load("recognizer\\trainingData.yml")
id=0
fontface=cv2.FONT_HERSHEY_DUPLEX
#fontscale=(1,1)
#fontcolor=(255,0,0)
while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        profile=getProfile(id)
        if(profile!=None):
            cv2.rectangle(img,(x,y+h+100),(x+w,y+h),(0,255,0),2);
            cv2.putText(img,str(profile[0]),(x,y+h+30),fontface,1,(0,255,0),2);
            cv2.putText(img,str(profile[1]),(x,y+h+60),fontface,1,(0,255,0),2);
            cv2.putText(img,str("%.1f"%(100.0-conf)+"%"),(x,y+h+90),fontface,1,(0,255,0),2);
    cv2.imshow("Face",img);
    if(cv2.waitKey(1)==ord('q')):
        break;
cam.release()
cv2.destroyAllWindows()
