

def collision(Coords1, Coords2):
        return not (
            Coords1[2] < Coords2[0] or  # Droite de obj1 à gauche de obj2
            Coords1[0] > Coords2[2] or  # Gauche de obj1 à droite de obj2
            Coords1[3] < Coords2[1] or  # Bas de obj1 au-dessus du haut de obj2
            Coords1[1] > Coords2[3]     # Haut de obj1 en dessous du bas de obj2
    )