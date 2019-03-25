import cv2,os
import numpy as np
from PIL import Image 
import pickle

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('C:\\Users\\DELL\\Desktop\\MicroProject\\trainer\\trainer.yml')
cascadePath = "C:\\Users\\DELL\\Desktop\\MicroProject\\Classifiers\\banana_classifier.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path = 'C:\\Users\\DELL\\Desktop\\MicroProject\\dataSet'

cam = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, im =cam.read()
    cv2.putText(im,"Banana",(100,100-10),font,0.55,(0,0,0),1)
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])
        cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
        if(nbr_predicted==1):
             nbr_predicted='ripe'
        #cv2.putText(im,nbr_predicted,(x,y+h),font,0.55,(0,255,0),2)
        cv2.imshow('im',im)
        cv2.waitKey(10)
