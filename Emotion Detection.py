import cv2
from deepface import DeepFace
from pymongo import MongoClient
from datetime import date

cluster = MongoClient(
    "mongodb+srv://<username>:<pass>@clusterh.lcaaf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"]

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    raise IOError("Cannot Open")

i = 5

while cam.isOpened():
    ret, frame = cam.read()

    predict = DeepFace.analyze(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    date1 = str(date.today())

    document = {"_id": i, "Emotion": predict['dominant_emotion'], "Gender": predict['gender'], "Date": date1}
    i = i + 1
    collection.insert_one(document)

    cv2.imshow('frame', frame)

    if cv2.waitKey(5) == ord('q'):
        break
