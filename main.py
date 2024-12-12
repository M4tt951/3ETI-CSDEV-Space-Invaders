import tkinter as tk
import random
import time

from Class_joueur import Joueur, protectionJoueur, Projectile
from Class_Aliens import Alien, LaserAlien




class Affichage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1200x800")
        self.root.title("Space Invaders")

        self.jeu_terminé = False

        self.longueur = 1200
        self.largeur = 800


        # Créer le canevas principal
        self.canvas = tk.Canvas(self.root, width=1200, height=800, bg="black")
        self.canvas.pack()

        # créer les potections 
        self.listeBloc1, self.listeBloc2, self.listeBloc3 = [], [], []
        self.listeBlocs = [self.listeBloc1, self.listeBloc2, self.listeBloc3]
        self.create_bloc(self.listeBloc1, 155, 533)
        self.create_bloc(self.listeBloc1, 540, 533)
        self.create_bloc(self.listeBloc1, 860, 533)



        # Créer les aliens
        self.aliens = []       #on remarque ici l'utilisation d'une liste ! permet de retrouver les coordonnées de chaque aliens.
        self.create_aliens(self.listeBlocs)


        # Créer le joueur/mouvement du joueur
        self.joueur = Joueur(self.canvas, 600, 700, largeur=50, longueur=20, vitesse=20)
        self.root.bind("<Left>", self.joueur.deplacer_gauche)
        self.root.bind("<Right>", self.joueur.deplacer_droite)
        self.root.bind("<KeyRelease-Left>", self.joueur.arret)
        self.root.bind("<KeyRelease-Right>", self.joueur.arret)
        self.root.bind("<space>", self.tirer_projectile)

        self.footer = tk.Canvas(self.root, width=self.longueur, height=60)
        self.footer.place(y=740)
        self.footer.configure(bg="black")

        self.footerGauche = tk.Canvas(self.footer, width=600, height=60, highlightthickness=0)
        self.footerGauche.pack(side="left")
        self.footerGauche.configure(bg="black")

        self.score = "Score : " + str(self.joueur.score)
        self.scoreAffichage = tk.Label(self.footerGauche, text=self.score, fg="white", bg="black", font=('Futura', 20), highlightthickness=5)
        self.scoreAffichage.pack(side="left")
        self.nbVies = str(self.joueur.coeur) + " Vies"
        self.nbViesAffichage = tk.Label(self.footerGauche, text=self.nbVies, fg="white", bg="black", font=('Futura', 20), highlightthickness=5)
        self.nbViesAffichage.pack(side="right")


        self.mise_a_jour_vie()
        self.mise_a_jour_score()

        self.footerDroite = tk.Canvas(self.footer, width=600, height=60, highlightthickness=0)
        self.footerDroite.pack(side="right")
        self.footerDroite.configure(bg="black")

        # bouton quitter 
        self.quitter = tk.Button(self.footer, text="Quitter", command=self.root.destroy, highlightthickness=0, border = 0, font=("futura", 20), fg="white", bg="black")
        self.quitter.pack(side = 'right', padx = 5, pady = 5)

        # bouton nouvelle partie 
        self.relaunch = tk.Button(self.footer, text="Rejouer ?", command=self.relaunch, highlightthickness=0, border = 0, font=("futura", 20), fg="white", bg="black")
        self.relaunch.pack(side="left", padx = 5, pady = 5)

        #Fait tirer les aliens
        self.aliens_tirent()

        self.root.after(2000, self.mise_a_jour_vie)
        self.root.mainloop()


    def mise_a_jour_vie(self):
        self.nbViesAffichage.config(text =f"{self.joueur.coeur}  Vies")
        self.nbViesAffichage.pack(side="right")
        self.root.after(200, self.mise_a_jour_vie)
        
    def mise_a_jour_score(self):
        self.scoreAffichage.config(text=f"Score : {self.joueur.score}")
        self.scoreAffichage.pack(side="left")
        self.root.after(200, self.mise_a_jour_score)


    def create_bloc(self, listeBloc, posX, posY) :
        ecart_blocs = 30
        nombre_lignes, nombre_colonnes = 3, 6

        for i in range(nombre_lignes) :
            for j in range(nombre_colonnes) :
                x = posX + 30 + j * ecart_blocs
                y = posY + 30 + i * ecart_blocs
                protec = protectionJoueur(self.canvas, x, y)
                listeBloc.append(protec)



    def create_aliens(self, liste_Blocs):
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
                alien = Alien(self.canvas, x, y, largeur=50, longueur=50, vitesse=vitesse, listeBlocs = liste_Blocs)
                self.aliens.append(alien)
                alien.deplacement()
    


    def aliens_tirent(self):
        if self.jeu_terminé:
            return
        if self.aliens: #si la liste existe encore
            alien = random.choice(self.aliens)
            alien.tirer_laser(self.joueur)
        self.root.after(random.randint(1000, 3000), self.aliens_tirent)

    def relaunch(self) :
        self.canvas.delete("all")

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


    def tirer_projectile(self, event):
        if self.jeu_terminé:
            return
        temps_init = time.time()
        print(self.joueur.dernier_tir)
        if temps_init - self.joueur.dernier_tir > 1 :
            joueur_coords = self.joueur.Position()
            x = (joueur_coords[0]+ joueur_coords[2]) / 2 #le projectile apparait au milieu du joueur
            y = joueur_coords[1]  # le projectile se place en haut du joueur

            projectile = Projectile(self.canvas, x - 5, y - 20, largeur = 10, longueur = 20, vitesse_proj = 10, aliens = self.aliens,  listeBlocs=self.listeBlocs, joueur =self.joueur)
            projectile.move()

            self.joueur.dernier_tir = temps_init

    def game_over(self):
        self.jeu_terminé = True

        print("la")

        self.canvas.create_rectangle(0, 0 , 1200, 800, fill ="red", outline ="red")
        self.canvas.create_text(600, 400, text=" Game Over ", fill = "red", font=("Purisan", 200))


# Lancer l'application
app = Affichage()