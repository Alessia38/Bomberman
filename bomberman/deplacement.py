from random import randint
import time
from affichage import afficher_plateau 
from variables_globales import score
import variables_globales
def deplacer_ennemi(plateau):
    directions = ['haut', 'bas', 'gauche', 'droite']
# Chercher tous les ennemis sur le plateau
    ennemis_positions = []
    for i, ligne in enumerate(plateau):
        for j, case in enumerate(ligne):
            if case == 'E':
                ennemis_positions.append((i, j))

# Déplacer chaque ennemi aléatoirement
    for x, y in ennemis_positions:
        direction = directions[randint(0, 3)]  # Choisir une direction aléatoire
        nouveau_x, nouveau_y = x, y

        if direction == 'haut' and x > 0:
            nouveau_x = x - 1
        elif direction == 'bas' and x < len(plateau) - 1:
            nouveau_x = x + 1
        elif direction == 'gauche' and y > 0:
            nouveau_y = y - 1
        elif direction == 'droite' and y < len(plateau[0]) - 1:
            nouveau_y = y + 1
        # Vérifier si la case cible est libre (pas de mur, ni autre ennemi, ni joueur)
        if plateau[nouveau_x][nouveau_y] == '.':
            plateau[x][y] = '.'  # Efface l'ancienne position de l'ennemi
            plateau[nouveau_x][nouveau_y] = 'E'  # Déplace l'ennemi à la nouvelle position

def deplacer_joueur(plateau, direction):
    """Déplace le joueur dans la direction indiquée (haut, bas, gauche, droite)."""
    variables_globales.score -= 5  # Déduit des points pour chaque déplacement
    # Trouver la position actuelle du joueur
    for i, ligne in enumerate(plateau):
        if 'J' in ligne:
            x, y = i, ligne.index('J')
            break
    else:
        print("Erreur : joueur non trouvé sur le plateau.")
        return

    # Définir la nouvelle position par défaut
    nouveau_x, nouveau_y = x, y

    # Déterminer la nouvelle position en fonction de la direction
    if direction == 'haut' and x > 0:
        nouveau_x = x - 1
    elif direction == 'bas' and x < len(plateau) - 1:
        nouveau_x = x + 1
    elif direction == 'gauche' and y > 0:
        nouveau_y = y - 1
    elif direction == 'droite' and y < len(plateau[0]) - 1:
        nouveau_y = y + 1
    else:
        print("Déplacement impossible.")
        return
    
    # Vérifier si la nouvelle position est occupée par un ennemi
    if plateau[nouveau_x][nouveau_y] == 'E':
        print("Vous avez rencontré un ennemi ! Partie perdue.")
        exit()  # Arrête le programme

    if plateau[nouveau_x][nouveau_y] == 'B':
        print("Vous avez rencontré un mur ! ")
        return
    # Déplacer le joueur vers la nouvelle position
    plateau[x][y] = '.'  # Efface l'ancienne position
    plateau[nouveau_x][nouveau_y] = 'J'  # Place le joueur dans la nouvelle position
    # Déduit des points pour chaque déplacement
    variables_globales.score -= 5

def poser_bombe(plateau, position_joueur):
    """Pose une bombe à la position actuelle du joueur."""
    x, y = position_joueur
    plateau[x][y] = 'O'  # Placer une bombe (symbole 'O' sur la case du joueur)
    afficher_plateau(plateau, variables_globales.score)

    # Simuler un délai avant l'explosion
    print("Bombe posée. Explosion dans 2 secondes...")
    time.sleep(2)

    # Gestion de l'explosion dans une croix autour de la bombe (haut, bas, gauche, droite)
    explosion(plateau, x, y)

    # Réapparaître le joueur à sa position si la bombe explose là où il était
    plateau[x][y] = 'J'

def explosion(plateau, x, y):
    """Gère l'explosion de la bombe : détruit les ennemis et les briques cassables."""
    def detruire_case(px, py):
        """Détruire une case si elle contient un ennemi ou une brique cassable."""
        if plateau[px][py] == 'E':
            print("Un ennemi a été détruit à la position", (px, py))
            variables_globales.score += 10 # Ajouter des points pour chaque ennemi détruit
        elif plateau[px][py] == 'B':
            print("Une brique cassable a été détruite à la position", (px, py))
            variables_globales.score += 5 # Ajouter des points pour chaque brique détruite
        plateau[px][py] = '.'  # Vider la case après destruction

    # Explosion sur 1 case à gauche, droite, haut, bas
    if x > 0:  # Haut
        detruire_case(x - 1, y)
    if x < len(plateau) - 1:  # Bas
        detruire_case(x + 1, y)
    if y > 0:  # Gauche
        detruire_case(x, y - 1)
    if y < len(plateau[0]) - 1:  # Droite
        detruire_case(x, y + 1)

    # Vider la case de la bombe après l'explosion
    plateau[x][y] = '.'
    afficher_plateau(plateau, variables_globales.score)