import face_recognition
import pickle
import mail
import numpy as np
#import serial
import time
import sys
import cv2

#use pickle to mine through dataset
mob=mail.mclass()

def compare_face():

    with open('dataset_faces.dat','rb') as f:
        all_face_encodings=pickle.load(f)

    #grab list of names and list of encodings

    face_names = list(all_face_encodings.keys())
    face_encodings = np.array(list(all_face_encodings.values()))


    #unlnown face encoding 

    unknown_image = face_recognition.load_image_file("./still.jpeg")
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    #get result of compared faces with encoding
    results = face_recognition.compare_faces(face_encodings, unknown_encoding)
    print(results)
    if True not in results:
        print("Unknown face detected")
        mob.multimediamail("Tresspasser alert from Home !!")
    #print result with list of names with true or false
    names_with_result=list(zip(face_names,results))
    print(names_with_result)

def detect_face():
    face_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
    print("iam here hello")
    #To capture the video stream from webcam.
    cap = cv2.VideoCapture(0)
    print("Getting camera image...") 
    cock=0
    while 1:

        ret, img = cap.read()
        cv2.namedWindow('img', cv2.WINDOW_NORMAL)
        #cv2.resizeWindow('img', 500,500)
        cv2.line(img,(500,250),(0,250),(0,255,0),1)
        cv2.line(img,(250,0),(250,500),(0,255,0),1)
        cv2.circle(img, (250, 250), 5, (255, 255, 255), -1)
        gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3)
        #fob=facerec.facedetect()

    #detect the face and make a rectangle around it.
        for (x,y,w,h) in faces:
            #print(faces)
            no_face=faces.shape[0]
            #print(" i found "+str(no_face)+" faces in the image")
            try:
                if(cock==50):
                    cv2.imwrite("still.jpeg", img)
                    compare_face()
                    break
              
                    
            except NameError: pass
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
            roi_gray  = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            cv2.imshow('img',img)

        #Hit 'Esc' to terminate execution
        if cock>50:
            break
        cock+=1



detect_face()


