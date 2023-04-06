import tkinter as tk
import os
import cv2
import sys
from PIL import Image, ImageTk


def max_known_faces():
    l = os.listdir('c:/lisa/rec_faciale/easy_facial_recognition-master/known_faces')
    liste = [x.split('.')[0] for x in l]
    return liste

num = list(map(int,max_known_faces()))

print(num)