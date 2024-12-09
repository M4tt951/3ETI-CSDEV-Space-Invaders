import tkinter as tk
from Collisions import collision



class Alien:
    def __init__(self, app, x, y, largeur, longueur, vitesse, listeBlocs):
        self.canvas = app
        self.x = x
        self.y = y
        self.largeur = 50
        self.longueur = 50
        self.vitesse = vitesse
        self.dx = vitesse
        self.dy = 0
        self.step_down = 50 # Distance de descente
        self.alien = self.canvas.create_rectangle(self.x, self.y, self.x + self.largeur, self.y + self.longueur, fill="red")
        self.listeBlocs = listeBlocs

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

        laser = LaserAlien(self.canvas, x - 5, y, largeur = 10, longueur = 20, vitesse = 5, affichage = self.canvas.master, listeBlocs = self.listeBlocs)
        laser.move(joueur)


class LaserAlien:
    def __init__(self, app, x, y, largeur, longueur, vitesse, affichage, listeBlocs):
        self.canvas = app
        self.x = x
        self.y = y 
        self.largeur = largeur
        self.longueur = longueur
        self.vitesse = vitesse
        self.affichage = affichage
        self.laser = self.canvas.create_rectangle( self.x, self.y , self.x + self.largeur, self.y + self.longueur, fill ="yellow")
        self.listeBlocs = listeBlocs


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
                self.affichage.game_over()

        self.canvas.after(20, self.move, joueur)

        for listeBloc in self.listeBlocs:
            for blocs in listeBloc :
                blocs_coords = self.canvas.coords(blocs.protection)
                if not blocs_coords:  # Skip if block has been deleted
                    continue
                if collision(laser_coords, blocs_coords):
                    self.canvas.delete(blocs.protection)
                    self.canvas.delete(self.laser)
                    self.blocs.remove(blocs)