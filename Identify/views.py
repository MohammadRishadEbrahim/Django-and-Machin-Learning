from django.shortcuts import render
from django.conf import settings
#import cv2 as cv
import numpy as np
import pandas as pd
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
#import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
import pickle
#from keras_facenet import FaceNet
from datetime import datetime
import pytz
import time
# Create your views here.
def indexView(request):
    return render(request,"Identify/index.html")

# def saveFrame(request,camera_name):
#     specific = "media/" + camera_name + "/"
#     save_dir = os.path.join(settings.MEDIA_ROOT,specific )
#     if not os.path.exists(save_dir):
#         os.makedirs(save_dir)

#     cap = cv.VideoCapture(0)
#     while True:
#         _ , frame = cap.read()
#         frame_name = os.path.join(save_dir,"frame.jpg")
#         cv.imwrite(frame_name, frame)
#         # cv.namedWindow("Display the Camera" , cv.WINDOW_NORMAL)
#         # cv.resizeWindow("Display the Camera")
#         cv.imshow("Display the Camera", frame,)
#         keyExit = cv.waitKey(5) & 0xFF
#         if keyExit == 27:
#             break
    
#     cap.release()
#     cv.destroyAllWindows()
   
#     return render(request,"identify/Camera.html",{
#                                                                "getActive" : "Active" ,
#                                                                  "strActive" : "Active" , 
#                                                                  "strNoActive" : "No Active" ,
#                                                                  "camera_name" : camera_name
#                                                                  })
    

# def getFrame(request,camera_name):
#     specific = "media/" + camera_name + "/"
#     get_dir = os.path.join(settings.MEDIA_ROOT,specific )
#     if not os.path.exists(get_dir):
#         os.makedirs(get_dir)

#     unkown_folder = "unkown" + "/"
#     unkown_dir = os.path.join(get_dir,unkown_folder )
#     if not os.path.exists(unkown_dir):
#         os.makedirs(unkown_dir)
    
#     name_time = time.time()
#     now_utc = datetime.now(pytz.utc)
#     afghanistan_tz = pytz.timezone('Asia/Kabul')
#     now_afghanistan = now_utc.astimezone(afghanistan_tz)

#     date_afghanistan = now_afghanistan.date()
#     time_afghanistan = now_afghanistan.time().replace(second=0, microsecond=0) 

#     #INITIALIZE
#     facenet = FaceNet()
#     faces_embeddings = np.load(str(settings.BASE_DIR.joinpath('Identify/path_to_haarcascade/faces_dataset.npz')))
    
#     Y = faces_embeddings['arr_1']
#     encoder = LabelEncoder()
#     encoder.fit(Y)

#     haarcascade = cv.CascadeClassifier(str(settings.BASE_DIR.joinpath('Identify/path_to_haarcascade/haarcascade_frontalface_default.xml')))
#     model = pickle.load(open(str(settings.BASE_DIR.joinpath('Identify/path_to_haarcascade/model_knn.pkl')), 'rb'))


#     cap = cv.VideoCapture(0)
#     # WHILE LOOP
#     tsh = 0.7
#     names = []
#     times = []
#     dates = []
#     unknown_counter = 0
#     while True:
#         _, frame = cap.read()
#         faces = haarcascade.detectMultiScale(frame, 1.3, 5)
#         for x,y,w,h in faces:
#             img = frame[y:y+h, x:x+w]
#             img = cv.resize(img, (160,160))
#             img = np.expand_dims(img,axis=0)
#             ypred = facenet.embeddings(img)
#             face_name = model.predict(ypred)
            
#             face_name = encoder.inverse_transform(face_name)[0]
#             prob = model.predict_proba(ypred)[0]

#             if max(prob) < tsh :
#                 cv.rectangle(frame, (x,y), (x+w,y+h), (0, 0, 255), 2)
#                 cv.putText(frame,"unkown",(x,y-10),cv.FONT_HERSHEY_SIMPLEX, 1,
#                        (0, 0, 255), 2)
                
#                 unknown_counter += 1  # Increment counter for unknown faces
#                 name_unknown = f"unknown_{unknown_counter}_{time.time()}"
#                 path = os.path.join(unkown_dir ,  name_unknown +".jpg")
#                 cv.imwrite(path, frame)

#             else:
#                 cv.rectangle(frame, (x,y), (x+w,y+h),  (0, 128, 0), 3)
#                 cv.putText(frame,str(face_name),(x,y-10) ,cv.FONT_HERSHEY_SIMPLEX, 1,
#                        (0, 128, 0), 2)
               

#                 if face_name not in names:
#                     names.append(face_name)
#                     times.append(time_afghanistan)
#                     dates.append(date_afghanistan)

#         info = {"Names": names, "Times" : times , "Dates" : dates}
#         info = pd.DataFrame(info)
#         info.to_csv(get_dir + camera_name+".csv",index=False,mode="a",header=False)
                
#         cv.imshow("Face Recognition", frame,)
#         keyExit = cv.waitKey(5) & 0xFF
#         if keyExit == 27:
#             break
#     cap.release()
#     cv.destroyAllWindows()

    

#     return render(request,"identify/Security.html",{
#                                                                "getActive" : "Active" ,
#                                                                  "strActive" : "Active" , 
#                                                                  "strNoActive" : "No Active" ,
#                                                                  "camera_name" : camera_name
#                                                                  })
