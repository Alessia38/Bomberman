from random import *
randomDirection = randint(1,4)
# Initialisation du tableau
def initialisation_plateau():
    """Initialise le plateau avec des ennemis (E), des briques (B), et un joueur (J)."""
    plateau = [
        ['.', '.', '.', '.', '.'],
        ['.', '.', 'E', 'B', '.'],
        ['.', '.', 'J', '.', '.'],
        ['.', '.', '.', 'E', '.'],
        ['.', '.', '.', '.', '.']
    ]
    return plateau