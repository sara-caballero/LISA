import tkinter as tk
import os
import cv2
import sys
from PIL import Image, ImageTk

# Retourne un tableau avec les noms de fichiers du dossier 
# known_faces au moment de l'execution sans l'extension
def files_known_faces():  
    fichiers = os.listdir('c:/projets_dev/lisa//known_faces')
    fichiersSansExtension = [x.split('.')[0] for x in fichiers]
    return fichiersSansExtension

# Covertit la liste du max_know_faces() en liste en int
num = list(map(int,files_known_faces()))  
max_photo = max(num)  #Stocke le max dans max_photo

def next_id_photo():
    id_photo = max_photo + 1
    return id_photo


id_photo = next_id_photo()

if __name__ == '__main__':   #si je veux pas que photo.py soit exécuté lorsque je l'importe dans inscription.py il faut mettre ça

    fileName = os.environ['ALLUSERSPROFILE'] + "\WebcamCap.txt"
    cancel = False


    def prompt_ok():
        global cancel, button, button1, button2
        cancel = True

        button.place_forget()
        button1 = tk.Button(mainWindow, text="C'est une bonne photo", command=saveAndExit)
        button2 = tk.Button(mainWindow, text="Réessayer", command=resume)
        button1.place(anchor=tk.CENTER, relx=0.2, rely=0.9, width=150, height=50)
        button2.place(anchor=tk.CENTER, relx=0.8, rely=0.9, width=150, height=50)
        button1.focus()


    def saveAndExit():
        global prevImg

        if len(sys.argv) < 2:
            filepath = "known_faces/" + str(id_photo) + ".jpg"  # chemin du repertoire où on veut mettre le fichier
        else:
            filepath = sys.argv[1]

        prevImg.save(filepath)
        mainWindow.quit()


    def resume():
        global button1, button2, button, lmain, cancel

        cancel = False

        button1.place_forget()
        button2.place_forget()

        mainWindow.bind('<Return>', prompt_ok)
        button.place(bordermode=tk.INSIDE, relx=0.5, rely=0.9, anchor=tk.CENTER, width=300, height=50)
        lmain.after(10, show_frame)


    try:
        f = open(fileName, 'r')
        camIndex = int(f.readline())
    except:
        camIndex = 0

    cap = cv2.VideoCapture(camIndex)
    capWidth = cap.get(3)
    capHeight = cap.get(4)

    success, frame = cap.read()

    mainWindow = tk.Tk(screenName="Camera Capture")
    mainWindow.resizable(width=False, height=False)
    mainWindow.bind('<Escape>', lambda e: mainWindow.quit())
    lmain = tk.Label(mainWindow, compound=tk.CENTER, anchor=tk.CENTER, relief=tk.RAISED)
    button = tk.Button(mainWindow, text="Capture", command=prompt_ok)

    lmain.pack()
    button.place(bordermode=tk.INSIDE, relx=0.5, rely=0.9, anchor=tk.CENTER, width=300, height=50)
    button.focus()


    def show_frame():
        global cancel, prevImg, button

        _, frame = cap.read()
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


        prevImg = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=prevImg)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        if not cancel:
            lmain.after(10, show_frame)



    show_frame()
    mainWindow.mainloop()
