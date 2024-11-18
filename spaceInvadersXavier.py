# UTF8
# Auteur : BROUSSOLLE Xavier
# Date de creation : 17/11/24
# Derniere maj : 17/11/24

################ - SPACE INVADERS - ################

### TO DO ###
"""
- deplacement bloc aliens 
- affichage aliens 
- affichage vaisseau 
- deplacement vaisseau 
- lancer projectile depuis vaisseau
- lancer projectiles depuis aliens 
- affichage et positionnement blocs de protection 
- comptage du score 
- comptage du nombre de vies 

"""


### Librairies ###
import tkinter as tk

class blocAliens() :
    def __init__(self) :
        self.largeur = 900
        self.longeur = 500
        self.position = deplacementBlocAlien()

    def renvoiDimensions(self) : 
        # fonction renvoyant le tuple des dimensions du bloc, pour pouvoir l'exploiter dans d'autres class ou fonctions
        return (self.largeur, self.longeur)


class alien() :
    def __init__(self, rang) : 
        self.rangAlien = rang
        self.largeur = 87
        self.longueur = 87
        self.vitesse = 10 
        self.imageAlien = tk.Canvas(self, width=self.largeur, height=self.longueur)


def deplacementBlocAlien(bloc, posxDepart, posyDepart) : 
    # fonction s'occupant du deplacement du bloc d'aliens
    # prend en argument la position en x et en y de depart
    # ainsi que le bloc d'aliens defini avec la classe blocAliens()
    # renvoie la position finale

    # initialisation des variables de position 
    posX = posxDepart
    posY = posyDepart


    # on parcourt les valeurs de position disponibles en x et en y
    for i in range(posxDepart, bloc.renvoiDimensions[0]) : 
        for j in range(posyDepart, bloc.renvoiDimensions[1]) : 
            # on atteint la limite a droite de la fenetre => on descend
            if posX == bloc.renvoiDimensions[0] :
                posY -= 20

            # on atteint la limite a gauche de la fenetre => on monte
            if posX == posxDepart :
                posY += 20

        

    nouvellePosition = (posX, posY)

    return nouvellePosition


class protectionJoueur() :
    def __init__(self, posx, posy) :
        # position en x et en y (en px), a l'interieur du bloc de protections
        self.posX = posx
        self.posY = posy
        # largeur et longueur de la protection (en px)
        self.longueur = 30
        self.largeur = 30
        # affichage de l'image de la protection 
        self.affichage = tk.Canvas(fenetre, width=self.largeur, height=self.longueur)
        # creation de l'image
        self.imageProtec = tk.PhotoImage(file="protec.png")
        # affichage de l'image dans le canva
        self.canvaVaisseau.create_image(self.posX, self.posY, anchor='n', image=self.imageProtec)


class blocProtectionsJoueur() : 
    def __init__(self, posx, posy, fenetre) : 
        self.fenetre = fenetre 
        
        # position en x et en y (en px)
        self.posX = posx
        self.posY = posy
        # largeur et longueur du bloc (en px)
        self.largeur = 200
        self.longueur = 80
        # nombre de protections en x et en y 
        self.nbProtecX = 6
        self.nbProtecY = 3
        # marges entre chaques petits blocs (en px)
        self.marginXProtec = 1 
        self.marginYProtec = 1 
        
        self.matrice = tk.Frame (self.fenetre.root, bd = 3, width = 180, height = 90)
        

    def matrice(self) : 
        self.cellules = []
        for i in range(6) :
            ligne = []
            for j in range(3) : 
                frame_cellule = tk.Frame(self.matrice, width=155, height=77)
                frame_cellule.grid(row=i, column=j, padx=1, pady=1)
                # affichage de l'image de la protection 
                self.protec = tk.Canvas(fenetre, width=self.largeur, height=self.longueur)
                # creation de l'image
                self.imageProtec = tk.PhotoImage(file="protec.png")
                # affichage de l'image dans le canva
                self.protec.create_image(self.posX, self.posY, anchor='n', image=self.imageProtec)
                ligne.append(self.imageProtec)
            
            self.cellules.append(ligne)
        
        return self.cellules


class vaisseauJoueur() :
    def __init__(self, posx, posy, fenetre) :
        # fenetre ou on va afficher le vaisseau 
        self.fenetre = fenetre 
        # position en x et en y (en px), au depart
        self.posX = posx
        self.posY = posy
        # largeur et longueur du vaisseau (en px)
        self.largeur = 155
        self.longueur = 77

        # affichage de l'image du vaisseau
        # creation du canva
        self.canvaVaisseau = tk.Canvas(self.fenetre.root, width=self.largeur, height=self.longueur)
        # creation de l'image
        self.imageVaisseau = tk.PhotoImage(file="vaisseau.png")
        # affichage de l'image dans le canva
        self.canvaVaisseau.create_image(self.posX, self.posY, anchor='n', image=self.imageVaisseau)

    def deplacementVaisseau(self, event) :
        # fonction permettant de deplacer le vaisseau du joueur avec les touches du clavier
        
        # recuperation de la touche choisie
        touche = event.keysym

        if touche == "Left" : 
            # deplacement du vaisseau de 20px vers la gauche
            self.posX -= 20

        if touche == "Right" : 
            # deplacement du vaisseau de 20px vers la droite
            self.posX += 20

        if touche == "Up" : 
            # deplacement du vaisseau de 20px vers le haut
            self.posY += 20

        if touche == "Down" : 
            # deplacement du vaisseau de 20px vers le bas
            self.posX -= 20

        # changement des coordonnees du vaisseau
        self.canvaVaisseau.coords(self.imageVaisseau, self.posX, self.posY)


def score() : 
    # fonction qui compte les points, le nombre de vie
    pass

def deplacementAlien() : 
    # fonction gerant le deplacement automatiques des aliens 
    pass
    
def lanceMissileJoueur() : 
    # fonction permettant au joueur de lancer un projectile 
    pass

def lanceMissileAlien() : 
    # fonction permettant aux aliens de lancer automatiquement des projectiles 
        pass

def impactAlien() : 
    # fonction permettant d'eliminer un alien lorsuq'il est touche par le projectile 
    pass


class fenetre() :
    def __init__(self) : 
        self.root = tk.Tk()

        self.nom = "Space Invaders"
        self.root.title(self.nom)

        # fenetre de dimension : 1200x800 px
        self.root.geometry('1200x800')

        # bouton quitter 
        self.quitter = tk.Button(self.root, text="Quitter", command=self.root.destroy)
        self.quitter.pack(side = 'bottom', padx = 5, pady = 5)

        

fenetreJeu = fenetre()

vaisseau1 = vaisseauJoueur(80, 80, fenetreJeu)

blocProtectionsJoueurGauche = blocProtectionsJoueur(100, 100, fenetreJeu)

fenetreJeu.root.mainloop()