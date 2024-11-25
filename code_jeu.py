import tkinter as tk

### ------------------------------------------------- ###
### SPACE INVADERS ###
# UTF8
# Auteurs : ARRIEU Matteo, BROUSSOLLE Xavier 
# Date de creation du fichier : Lundi 4 Nov 2024
# Derniere mise a jour : Lundi 4 Nov 2024
### ------------------------------------------------- ###

import tkinter as tk
import random
import time

class Joueur:
    def __init__(self, canvas, x, y, largeur, longueur, vitesse):
        self.canvas = canvas  # Référence au canevas principal
        self.x = x
        self.y = y
        self.largeur = largeur
        self.longueur = longueur
        self.vitesse = vitesse
        self.direction = 0
        self.coeur = 3
        self.dernier_tir = 0

        # Créer le joueur comme un rectangle
        self.joueur = self.canvas.create_rectangle(
            self.x, self.y,
            self.x + self.largeur, self.y + self.longueur,
            fill="blue")

        self.mouvement_continue()
        
    

    def deplacer_gauche(self, event):
        # Déplace le joueur à gauche, avec une limite
        self.direction = -1

    def deplacer_droite(self, event):
        # Déplace le joueur à droite, avec une limite
        self.direction = 1

    def arret(self, event):
        self.direction = 0

    def Position(self):
        return(self.canvas.coords(self.joueur))    
    
    
    def mouvement_continue(self):
        if self.direction != 0:
            coords = self.canvas.coords(self.joueur)

            if self.direction == -1 and coords[0] > 0:
                self.canvas.move(self.joueur, -self.vitesse, 0)
            elif self.direction == 1 and coords[2] < 1200:
                self.canvas.move(self.joueur, self.vitesse, 0)

        self.canvas.after(20, self.mouvement_continue)

    

class Alien:
    def __init__(self, canvas, x, y, largeur, longueur, vitesse):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.largeur = 50
        self.longueur = 50
        self.vitesse = vitesse
        self.dx = vitesse
        self.dy = 0
        self.step_down = 50 # Distance de descente
        self.alien = self.canvas.create_rectangle(self.x, self.y, self.x + self.largeur, self.y + self.longueur, fill="red")

    def deplacement(self):
        coords = self.canvas.coords(self.alien)
        # Déplacement horizontal
        if self.dx != 0:
            self.y = coords[1]
            if (coords[0] <= 0 and self.dx < 0) or (coords[2] >= 1200 and self.dx > 0):  # Limites gauche/droite
                self.dx = 0
                self.dy = self.vitesse  # Commencer à descendre
            else:  
                self.canvas.move(self.alien, self.dx, 0)

        # Déplacement vertical (descente)
        if self.dy != 0:
            # Vérifier si l'alien a atteint la limite de descente
            if coords[1] >= self.y + self.step_down:  # Si l'alien a descendu de la distance définie
                self.dy = 0  # Arrêter la descente
                # Inverser la direction horizontale (dx)
                if coords[0] <= 0:
                    self.dx = self.vitesse
                else:
                    self.dx = - self.vitesse
            else:
                self.canvas.move(self.alien, 0, self.dy)

                

        # Répéter le mouvement
        self.canvas.after(10, self.deplacement)

    def tirer_laser(self, joueur):
        coords = self.canvas.coords(self.alien)
        x = (coords[0]+coords[2])/2
        y = coords[3]

        laser = LaserAlien(self.canvas, x - 5, y, largeur = 10, longueur = 20, vitesse = 5)
        laser.move(joueur)



def collision(Coords1, Coords2):
        return not (
            Coords1[2] < Coords2[0] or  # Droite de obj1 à gauche de obj2
            Coords1[0] > Coords2[2] or  # Gauche de obj1 à droite de obj2
            Coords1[3] < Coords2[1] or  # Bas de obj1 au-dessus du haut de obj2
            Coords1[1] > Coords2[3]     # Haut de obj1 en dessous du bas de obj2
    )

class Projectile:
    def __init__(self, canvas, x, y, largeur, longueur, vitesse_proj, aliens):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.largeur = 10
        self.longueur = 30
        self.vitesse = vitesse_proj
        self.aliens = aliens


        self.projectile = self.canvas.create_rectangle(self.x, self.y,self.x + self.largeur, self.y + self.longueur,fill="yellow")



    def move(self):
        self.canvas.move(self.projectile, 0, -self.vitesse)

        projectile_coords = self.canvas.coords(self.projectile)

        
        if projectile_coords[1] < 0:
            self.canvas.delete(self.projectile)
            

        for aliens in self.aliens:
            aliens_coords = self.canvas.coords(aliens.alien)
            if collision(projectile_coords, aliens_coords):
                self.canvas.delete(aliens.alien)
                self.canvas.delete(self.projectile)
                self.aliens.remove(aliens)
        self.canvas.after(20, self.move)

class LaserAlien:
    def __init__(self, canvas, x, y, largeur, longueur, vitesse):
        self.canvas = canvas
        self.x = x
        self.y = y 
        self.largeur = largeur
        self.longueur = longueur
        self.vitesse = vitesse
        self.laser = self.canvas.create_rectangle( self.x, self.y , self.x + self.largeur, self.y + self.longueur, fill ="yellow")

    def move(self, joueur):
        self.canvas.move(self.laser, 0 ,self.vitesse)
        laser_coords = self.canvas.coords(self.laser)

        if laser_coords[3] > 800:
            self.canvas.delete(self.laser)
            return
        
        joueur_coords = joueur.Position()
        if collision(laser_coords, joueur_coords):
            self.canvas.delete(self.laser)
            joueur.coeur = joueur.coeur - 1
            if joueur.coeur == 0:
                self.canvas.delete(joueur.joueur)
                Affichage.game_over()

        self.canvas.after(20, self.move, joueur)
        

        


class Affichage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1200x800")
        self.root.title("Space Invaders")

        self.jeu_terminé = False


        # Créer le canevas principal
        self.canvas = tk.Canvas(self.root, width=1200, height=800, bg="black")
        self.canvas.pack()

        # Créer les aliens
        self.aliens = []       #on remarque ici l'utilisation d'une liste ! permet de retrouver les coordonnées de chaque aliens.
        self.create_aliens()


        # Créer le joueur/mouvement du joueur
        self.joueur = Joueur(self.canvas, 600, 700, largeur=50, longueur=20, vitesse=20)
        self.root.bind("<Left>", self.joueur.deplacer_gauche)
        self.root.bind("<Right>", self.joueur.deplacer_droite)
        self.root.bind("<KeyRelease-Left>", self.joueur.arret)
        self.root.bind("<KeyRelease-Right>", self.joueur.arret)
        self.root.bind("<space>", self.tirer_projectile)

        #Fait tirer les aliens
        self.aliens_tirent()



        self.root.mainloop()


    def create_aliens(self):
        if self.jeu_terminé:
            return
        vitesse = 3
        alien_spacing_x = 100  # Espacement horizontal
        alien_spacing_y = 70   # Espacement vertical
        num_rows = 3
        num_columns = 5

        for row in range(num_rows):
            for col in range(num_columns):
                x = 100 + col * alien_spacing_x
                y = 50 + row * alien_spacing_y
                alien = Alien(self.canvas, x, y, largeur=50, longueur=50, vitesse=vitesse)
                self.aliens.append(alien)
                alien.deplacement()
    
    def aliens_tirent(self):
        if self.jeu_terminé:
            return
        if self.aliens: #si la liste existe encore
            alien = random.choice(self.aliens)
            alien.tirer_laser(self.joueur)
        self.root.after(random.randint(1000, 3000), self.aliens_tirent)

    def tirer_projectile(self, event):
        if self.jeu_terminé:
            return
        temps_init = time.time()
        print(self.joueur.dernier_tir)
        if temps_init - self.joueur.dernier_tir > 1 :
            joueur_coords = self.joueur.Position()
            x = (joueur_coords[0]+ joueur_coords[2]) / 2 #le projectile apparait au milieu du joueur
            y = joueur_coords[1]  # le projectile se place en haut du joueur

            projectile = Projectile(self.canvas, x - 5, y - 20, largeur = 10, longueur = 20, vitesse_proj = 10, aliens = self.aliens)
            projectile.move()

            self.joueur.dernier_tir = temps_init

    def game_over(self):
        self.jeu_terminé = True

        self.canvas.create_rectangle(0, 0 , 1200, 800, fill ="black", outline ="black")
        self.canvas.create_text(600, 400, text=" Game Over ", fill = "red", font=("Times new roman", 200))


# Lancer l'application
app = Affichage()



    








