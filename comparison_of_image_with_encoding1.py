import face_recognition
import mail
import pickle
import numpy as np
import cv2
#import random
import os


mob=mail.mclass()

#emotion_choice=["sad","angry","normal","happy"]
#use pickle to mine through dataset
class facedetect:
    
    def __init__(cls):
        with open("./dataset_faces.dat",'rb') as f:
            all_face_encodings=pickle.load(f)

        #grab list of names and list of encodings

        cls.face_names = list(all_face_encodings.keys())
        cls.face_encodings = np.array(list(all_face_encodings.values()))
        
    def unknownface(cls,image):
        cls.image=image
         # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(image, (0, 0), fx=0.25, fy=0.25)
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        
        #unknown_image = face_recognition.load_image_file(image)
        cls.unknown_encoding = face_recognition.face_encodings(rgb_small_frame,face_locations)
        cv2.imwrite("./still.jpeg",image)
        print("image wrote")
    
    def printname(self,num):
        print(" found "+str(num)+" faces in the image")
        if not self.unknown_encoding:
            print("unknown")
            #cv2.imwrite("still.jpeg",cls.image)
            #os.system("raspistill -o /home/pi/Public/ms_proj_homeautomation/tress/still.jpeg")
            #os.system("espeak -ven-us+f4 -s155 'unknown face detected   Tresspasser ALERT '")
            print("unknown face detected mail will be sent to satya")
            mob.multimediamail("Tresspasser allert from Home !!")
        else:
            count=0
            li=[]
            #emotiondic={}
            results = face_recognition.compare_faces(self.face_encodings, self.unknown_encoding)
            names_with_result=list(zip(self.face_names,results))
            for i in names_with_result:
                if i[1]==True:
                    count+=1
                    li.append(i[0])
                    #emotiondic[i[0]]=random.choice(emotion_choice)
                    if count ==num:
                        break
                    
            string_name="hello "+" and ".join(li)
            cmd="espeak -ven-us+f4 -s155 \'"+string_name+"\'"
            print(string_name)
            #os.system(cmd)
