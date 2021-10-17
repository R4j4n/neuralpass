from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime
import PIL
import cv2
import numpy as np
import mtcnn
from architecture import *
import pickle
import quant
import GetKey
from path import facenet_weight,encodigs_path,camera
from PIL import Image, ImageTk
from cryptography.fernet import Fernet
from train_v2 import normalize, l2_normalizer
from scipy.spatial.distance import cosine
from tensorflow.keras.models import load_model

# creates a Tk() object
master = Tk()
master.bind('<Escape>', lambda e: root.quit())
lmain = Label(master)
lmain.pack()
# sets the geometry of main
# root window
master.geometry("1400x700+0+0")
master.title(" Neural password system")

my_img = ImageTk.PhotoImage(Image.open("media\\firstui2.png"))
master.iconbitmap("media\\neuralnet.ico")
my_label = Label(master, image=my_img)
my_label.pack()


def openNewWindow():

    confidence_t = 0.99
    recognition_t = 0.5
    required_size = (160, 160)

    def get_face(img, box):
        x1, y1, width, height = box
        x1, y1 = abs(x1), abs(y1)
        x2, y2 = x1 + width, y1 + height
        face = img[y1:y2, x1:x2]
        return face, (x1, y1), (x2, y2)

    def get_encode(face_encoder, face, size):
        face = normalize(face)
        face = cv2.resize(face, size)
        encode = face_encoder.predict(np.expand_dims(face, axis=0))[0]
        return encode

    def load_pickle(path):
        with open(path, 'rb') as f:
            encoding_dict = pickle.load(f)
        return encoding_dict

    def most_frequent(List):
        counter = 0
        num = List[0]

        for i in List:
            curr_frequency = List.count(i)
            if(curr_frequency > counter):
                counter = curr_frequency
                num = i

        return num

    def detect(img, detector, encoder, encoding_dict, x):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = detector.detect_faces(img_rgb)
        for res in results:
            if res['confidence'] < confidence_t:
                continue
            face, pt_1, pt_2 = get_face(img_rgb, res['box'])
            encode = get_encode(encoder, face, required_size)
            encode = l2_normalizer.transform(encode.reshape(1, -1))[0]
            name = 'unknown'

            distance = float("inf")
            for db_name, db_encode in encoding_dict.items():
                dist = cosine(db_encode, encode)
                if dist < recognition_t and dist < distance:
                    name = db_name
                    distance = dist

            if name == 'unknown':
                cv2.rectangle(img, pt_1, pt_2, (0, 0, 255), 2)
                cv2.putText(img, name, pt_1, cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 0, 255), 1)
            else:
                cv2.rectangle(img, pt_1, pt_2, (0, 255, 0), 2)
                cv2.putText(img, name + f'__{distance:.2f}', (pt_1[0], pt_1[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0, 200, 200), 2)
            x = name
        return img, x

    if __name__ == "__main__":
        required_shape = (160, 160)
        face_encoder = InceptionResNetV2()
        face_encoder.load_weights(facenet_weight)
        face_detector = mtcnn.MTCNN()
        encoding_dict = load_pickle(encodigs_path)
        x = ''
        cap = cv2.VideoCapture(1)
        count = 0
        final = []
        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                print("CAM NOT OPEND")
                break

            frame, identity = detect(frame, face_detector,
                                     face_encoder, encoding_dict, x)
            if identity == 'unknown' or identity == '':
                cv2.putText(frame, "FACE NOT DETECTED", (5, 60),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

            else:
                count += 1
                final.append(identity)
                cv2.putText(frame, "Collecting Face Samples", (5, 30),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                cv2.putText(frame, str(5-count), (300, 60),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

            cv2.imshow('camera', frame)
            print(identity)
            if cv2.waitKey(1) & 0xFF == ord('q') or count == 5:
                cap.release()
        cv2.destroyWindow('camera')
        face_result = most_frequent(final)
        print(face_result)
        cap_eye = cv2.VideoCapture(1)
        quant.mainquant(face_result)


label = Label(master,
              text="Welcome to the NEURAL PASS\n  Secure password management system based on face and eye pattern recognization system\n\n We need to scan your face in order to continue.", font=('arial', 20, 'bold'), fg='black')

label.pack(pady=10)

# a button widget which will open a
# new window on button click
btn = Button(master,
             text="Authenticate your face", width=18, font=('arial', 20, 'bold'), fg='red', command=openNewWindow)
btn.pack(pady=10)

# mainloop, runs infinitely
mainloop()
