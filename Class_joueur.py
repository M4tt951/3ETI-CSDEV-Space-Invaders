from Collisions import collision


class Joueur:
    def __init__(self, app, x, y, largeur, longueur, vitesse):
        self.canvas = app  # Référence au canevas principal
        self.x = x
        self.y = y
        self.largeur = largeur
        self.longueur = longueur
        self.vitesse = vitesse
        self.direction = 0
        self.score = 0
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



class protectionJoueur : 
    def __init__(self, canvas, posx, posy) : 
        self.canvas = canvas 
        
        self.posX = posx
        self.posY = posy

        self.longueur = 30
        self.largeur = 30
        
        self.protection = self.canvas.create_rectangle(self.posX, self.posY, self.posX + self.largeur, self.posY + self.longueur, fill="yellow")


class Projectile:
    def __init__(self, app, x, y, largeur, longueur, vitesse_proj, aliens, listeBlocs, joueur):
        self.canvas = app
        self.x = x
        self.y = y
        self.largeur = 10
        self.longueur = 30
        self.vitesse = vitesse_proj
        self.aliens = aliens
        self.listeBlocs = listeBlocs
        self.joueur = joueur


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
                self.joueur.score = self.joueur.score + 100
        self.canvas.after(20, self.move)

        for listeBloc in self.listeBlocs:
            for blocs in listeBloc :
                blocs_coords = self.canvas.coords(blocs.protection)
                if not blocs_coords:  # Skip if block has been deleted
                    continue
                if collision(projectile_coords, blocs_coords):
                    self.canvas.delete(blocs.protection)
                    self.canvas.delete(self.projectile)
                    self.blocs.remove(blocs)