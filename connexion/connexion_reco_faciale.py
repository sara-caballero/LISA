#import easy_facial_recognition
import os

def lancer_rec_faciale():
    os.system("easy_facial_recognition.py --i known_faces")

lancer_rec_faciale()

id = easy_facial_recognition.easy_face_reco()