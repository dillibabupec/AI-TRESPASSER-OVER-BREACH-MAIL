import face_recognition
import pickle
#import numpy as np

all_face_encodings={}

#add encoding to dictionary
yadav_image = face_recognition.load_image_file("./images/Yadav.jpeg")
all_face_encodings["yadav"] = face_recognition.face_encodings(yadav_image)[0]
# yadav_image = face_recognition.load_image_file("./images/ganga.jpeg")
# all_face_encodings["ganga"] = face_recognition.face_encodings(yadav_image)[0]
# yadav_image = face_recognition.load_image_file("./images/pysc.jpeg")
# all_face_encodings["pysc"] = face_recognition.face_encodings(yadav_image)[0]


#dump encoding to dat file named "dataset_faces"

with open('dataset_faces.dat','wb') as f:
    pickle.dump(all_face_encodings,f)
