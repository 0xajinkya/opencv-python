import os
import cv2 as cv
import numpy as np

people = ['Henry Cavil', 'Hrithik Roshan', 'Allu Arjun', 'Christian Bale', 'Mrunal Thakur']

# p = []

# for i in os.listdir(r'/home/ajinkya/face_recognition'):
#     p.append(i)

# print(p)

DIR = r'/home/ajinkya/face_recognition'

haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)  # type: ignore
                labels.append(label)  # type: ignore

create_train()
print('Training Done')

features = np.array(features, dtype='object')
labels = np.array(labels)


face_recognizer = cv.face.LBPHFaceRecognizer_create()


#Training The Recognizer On The Features List And The Labels List

face_recognizer.train(features, labels)
face_recognizer.save('face_trained.yml')

np.save('features.npy', features)
np.save('labels.npy', labels)






