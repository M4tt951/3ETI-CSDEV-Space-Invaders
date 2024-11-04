import tkinter as tk
class Affichage:
        def __init__(self): 
            self.mw=tk.Tk()
            self.mw.title("Space Invaders")
            self.mw.geometry('1200x830')
            Titre = tk.Label(self.mw, text="Space Invaders", fg = 'black')
            Titre.pack(pady= 10)
            button_options = tk.Button(self.mw, text ="Options", fg='black')
            button_options.pack(pady =100)
            buttonquit = tk.Button(self.mw, text="Quitter", fg='red', command=self.mw.quit)
            buttonquit.pack(pady=50)
            self.mw.mainloop()

Affichage()
