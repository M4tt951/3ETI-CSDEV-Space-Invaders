import tkinter as tk

### ------------------------------------------------- ###
### SPACE INVADERS ###
# UTF8
# Auteurs : ARRIEU Matteo, BROUSSOLLE Xavier 
# Date de creation du fichier : Lundi 4 Nov 2024
# Derniere mise a jour : Lundi 4 Nov 2024
### ------------------------------------------------- ###

class Affichage:
    def __init__(self):
        self.mw = tk.Tk()
        self.mw.title("Space Invaders")
        self.mw.geometry('1200x830')

        # Creation of an alien object in the Affichage class
        self.alien = Alien(self.mw)

        # Start the main loop
        self.mw.mainloop()

class Alien:
    def __init__(self, root):
        # Alien's initial settings
        self.largeur = 87
        self.longueur = 87
        self.vitesse = 10
        self.x = 100
        self.y = 100
        self.dx = self.vitesse
        self.dy = 0

        # Create the canvas for the alien
        self.AlienCanvas = tk.Canvas(root, width=self.largeur, height=self.longueur, bg='red')
        self.AlienCanvas.place(x=self.x, y=self.y)

        # Start the movement
        self.deplacement()

    def deplacement(self):
        # Update position based on direction
        self.x = self.x + self.dx
        self.y = self.y + self.dy

        # Check boundaries and update direction
        if self.x <= 20:  # Left limit
            limit = self.y
            while self.y < limit + 100:
                self.dx = 0
                self.dy= self.vitesse
            self.dx = - self.vitesse
        elif self.x >= 1113:  # Right limit (1200 - self.largeur)
            limit = self.y
            while self.y < limit + 100:
                self.dx = 0
                self.dy= self.vitesse
            self.dx = - self.vitesse

        # Update the position on the canvas
        self.AlienCanvas.place(x=self.x, y=self.y)

        # Repeat the movement every 20 ms
        self.AlienCanvas.after(20, self.deplacement)

# Run the Affichage class to start the application
app = Affichage()
