import tkinter as tk
from PIL import Image, ImageTk
class Affichage:
        def __init__(self): 
            self.mw=tk.Tk()
            self.mw.title("Space Invaders")
            self.mw.geometry('1270x830')
            image_chemin ="..//3ETI-CSDEV-SPACE-INVADERS-1/images/Espace_Background.jpg"
            img1 = Image.open(image_chemin)
            bg = ImageTk.PhotoImage(img1)
            Logo_chemin="../3ETI-CSDEV-SPACE-INVADERS-1/images/Logo_Space_Invaders.jpeg"
            img2 = Image.open(Logo_chemin)
            img2 = img2.resize((200, 200))
            lg = ImageTk.PhotoImage(img2)

            background_label = tk.Label(self.mw, image = bg)
            background_label.image = bg
            background_label.place(x = 0, y = 0, relwidth=1, relheight = 1)

            Logo_label = tk.Label(self.mw, image = lg, bg = None)
            Logo_label.image = lg
            Logo_label.place(x = 540, y = 100)

            Start_game = tk.Button(self.mw, text="Commencer la partie", fg ='black', width =20, height = 3)
            Start_game.place( x = 570 , y = 350)

            button_options = tk.Button(self.mw, text ="Options", fg='black', width =20, height = 3)
            button_options.place(x = 570, y = 450)

            buttonquit = tk.Button(self.mw, text="Quitter", fg='red', command=self.mw.quit, width =20, height = 3)
            buttonquit.place(x = 570 , y = 550)

            self.mw.mainloop()

Affichage()
