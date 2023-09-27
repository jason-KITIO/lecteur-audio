from tkinter import *
from tkinter import filedialog, messagebox
from pathlib import Path

import tkinter as tk

import os
import pygame

pygame.init()

# interface
window = tk.Tk()
window.title("Lecteur")
window.geometry("900x565")
window.minsize(700, 565)
window.iconbitmap("image/icone.ico")
window.config(background="#5394cc", border=0)
frame = Frame(window, background="#5394cc")
sousFrame1 = Frame(frame, background="#5394cc")
sousFrame2 = Frame(frame, background="#d1a0a0", border=10, relief=SUNKEN)
sousFrame3 = Frame(frame, background="#cfb5ca")
# --------------------------------------------------debut image------------------------------------------------------

# droite
photo1 = tk.PhotoImage(file="image/gauche2.png").zoom(15).subsample(25)
# pause
photo2 = tk.PhotoImage(file="image/pause1.png").zoom(5).subsample(25)
# jouer
photo3 = tk.PhotoImage(file="image/play1.png").zoom(5).subsample(25)
# gauche
photo4 = tk.PhotoImage(file="image/droite2.png").zoom(15).subsample(25)


# --------------------------------------------------fin image------------------------------------------------------


def close_window():
    window.destroy()


def show_dialog():
    messagebox.showinfo(f"About", """Developper par jason kitio © 2023\n
Email : kanamax00@outlook.fr / kanamax00@gmail.com\n
Contact : +237 696 354 128 / +237 621 289 159\n
Merci d'avoir utiliser mon application \u2764\n
                        """)


# --------------------------------------------------debut fonction------------------------------------------------------
liste = []
chemin = ""


# ouvrir l'explorateur windows
def openfile():
    global liste
    global chemin
    fichier = filedialog.askdirectory()
    listeFichier = os.listdir(fichier)
    print(fichier)
    # pprint(listeFichier)
    liste = listeFichier
    chemin = fichier
    return listeFichier
    # return filedialog.askopenfilename()


openfile()
print(liste)
for i in liste:
    file_path = Path(i)
    extension = file_path.suffix
    if not extension == ".mp3":
        liste.remove(i)
print(liste)

# print(chemin)
sounds = {}

for index, item in enumerate(liste):
    sounds[str(index)] = item

print(sounds.items())

name = 0


def test():
    file = chemin + "/" + sounds[str(name)]
    print(file)
    # search.insert(0, sounds[name])
    # print(sounds[0])
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    pygame.event.wait()
    search.insert(0, sounds[str(name)])


def pauseMusique():
    pygame.mixer.music.pause()


def jouerMusique():
    pygame.mixer.music.unpause()


def musiqueSuivante():
    global name
    name += 1
    test()


def musiquePrecedente():
    global name
    name -= 1
    test()


# --------------------------------------------------fin fonction------------------------------------------------------

# menu
menu = Menu(window)

file_Fichier = Menu(menu, tearoff=0)
file_Fichier.add_command(label="Ouvrir", command=openfile)
file_Fichier.add_command(label="Quitter", command=close_window)

file_about = Menu(menu, tearoff=0)
file_about.add_command(label="Detail", command=show_dialog)

menu.add_cascade(label="Fichier", menu=file_Fichier)
menu.add_cascade(label="About", menu=file_about)
# texte1
label_Titre = Label(sousFrame1, text="Bienvenue", font=("HELVERIA", 40), bg="#5394cc", fg="White")
label_Titre.pack(fill=X, pady=25)

label_Titre = Label(sousFrame1, text="veillez cliquer sur un bouton pour jouer la musique ", font=("HELVERIA", 20),
                    bg="#5394cc", fg="White")
label_Titre.pack(fill=X)

"""#texte2
label_Titre = Label(sousFrame2, text="Mots de passe", font=("HELVERIA", 40), bg="#5394cc", fg="White")
label_Titre.pack(fill=X, pady=100)
#ajouter un input/entrer/"""
# zone de texte
search = Entry(sousFrame2, font=("HELVERIA", 20), bg="#757575", fg="White", width=37)
search.pack(fill=X, pady=100, padx=30)

# insertion des image
coleurImage = "#c79ebf"
width = 100
height = 100

bouton = Button(sousFrame3, image=photo1, width=width, height=height, command=musiquePrecedente)
bouton.grid(row=0, column=1, sticky=W, padx=25, pady=10)

bouton = Button(sousFrame3, image=photo2, width=width, height=height, command=pauseMusique)
bouton.grid(row=0, column=2, padx=25, pady=10)

bouton = Button(sousFrame3, image=photo3, width=width, height=height, command=jouerMusique)
bouton.grid(row=0, column=3, padx=25, pady=10)

bouton = Button(sousFrame3, image=photo4, width=width, height=height, command=musiqueSuivante)
bouton.grid(row=0, column=4, sticky=E, padx=25, pady=10)

# afficher l'interface
window.config(menu=menu)

sousFrame1.pack()
sousFrame2.pack(pady=15)
sousFrame3.pack(fill=X, )

frame.pack(expand=YES)
window.mainloop()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
