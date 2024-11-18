import tkinter as tk

### ------------------------------------------------- ###
### SPACE INVADERS ###
# UTF8
# Auteurs : ARRIEU Matteo, BROUSSOLLE Xavier 
# Date de creation du fichier : Lundi 4 Nov 2024
# Derniere mise a jour : Lundi 4 Nov 2024
### ------------------------------------------------- ###

import tkinter as tk

class Joueur:
    def __init__(self, canvas, x, y, largeur, longueur, vitesse):
        self.canvas = canvas  # Référence au canevas principal
        self.x = x
        self.y = y
        self.largeur = largeur
        self.longueur = longueur
        self.vitesse = vitesse

        # Créer le joueur comme un rectangle
        self.joueur = self.canvas.create_rectangle(
            self.x, self.y,
            self.x + self.largeur, self.y + self.longueur,
            fill="blue"
        )

    def deplacer_gauche(self, event):
        # Déplace le joueur à gauche, avec une limite
        if self.canvas.coords(self.joueur)[0] > 0:
            self.canvas.move(self.joueur, -self.vitesse, 0)

    def deplacer_droite(self, event):
        # Déplace le joueur à droite, avec une limite
        if self.canvas.coords(self.joueur)[2] < 1200:
            self.canvas.move(self.joueur, self.vitesse, 0)

class Alien:
    def __init__(self, canvas, x, y, largeur, longueur, vitesse):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.largeur = 50
        self.longueur = 50
        self.vitesse = 1
        self.dx = 10
        self.dy = 0
        self.step_down = 50  # Distance de descente
        self.alien = self.canvas.create_rectangle(self.x, self.y, self.x + self.largeur, self.y + self.longueur, fill="red")
        
    def deplacement(self):
        coords = self.canvas.coords(self.alien)
        print(coords[1])

        # Déplacement horizontal
        if self.dx != 0:
            if coords[0] <= 0 or coords[2] >= 1200:  # Limites gauche/droite
                self.dx = 0
                self.dy = self.step_down  # Commencer à descendre
            else:
                self.canvas.move(self.alien, self.dx, 0)

        # Déplacement vertical (descente)
        if self.dy > 0:
            self.canvas.move(self.alien, 0, self.dy)
            coords = self.canvas.coords(self.alien)
            if coords[1] >= self.y + self.step_down:  # Si on a atteint la limite de descente
                self.dy = 0
                self.dx = -self.vitesse if self.dx > 0 else self.vitesse  # Inverser la direction horizontale

        # Répéter le mouvement
        self.canvas.after(20, self.deplacement)

class Affichage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1200x800")
        self.root.title("Space Invaders")

        # Créer le canevas principal
        self.canvas = tk.Canvas(self.root, width=1200, height=800, bg="black")
        self.canvas.pack()

        # Créer les aliens
        self.aliens = []
        self.create_aliens()

        # Créer le joueur
        self.joueur = Joueur(self.canvas, 600, 700, largeur=50, longueur=20, vitesse=20)
        self.root.bind("<Left>", self.joueur.deplacer_gauche)
        self.root.bind("<Right>", self.joueur.deplacer_droite)

        # Lancer la boucle principale
        self.root.mainloop()

    def create_aliens(self):
        vitesse=10
        alien_spacing_x = 100  # Espacement horizontal
        alien_spacing_y = 70   # Espacement vertical
        num_rows = 3
        num_columns = 5

        for row in range(num_rows):
            for col in range(num_columns):
                x = 100 + col * alien_spacing_x
                y = 50 + row * alien_spacing_y
                alien = Alien(self.canvas, x, y, largeur=50, longueur=50, vitesse=5)
                self.aliens.append(alien)
                alien.deplacement()

# Lancer l'application
app = Affichage()






