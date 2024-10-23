import time

# Initialisation du tableau avec des ennemis (E) à des positions fixes
plateau = [
    ['.', '.', '.', '.', '.'],
    ['.', '.', 'E', 'B', '.'],
    ['.', '.', 'J', '.', '.'],
    ['.', '.', '.', 'E', '.'],
    ['.', '.', '.', '.', '.']
]

def afficher_plateau(plateau):
    """Affichage du tableau."""
    for ligne in plateau:
        print(' '.join(ligne))

def deplacer_joueur(plateau, direction):
    """Déplace le joueur dans la direction indiquée (haut, bas, gauche, droite)."""
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

def poser_bombe (plateau, position_joueur):
    x, y = position_joueur
    plateau[x][y] = 'X'
    afficher_plateau(plateau)

    print("Bombe posée. Explosion d'ici 2 secondes...")
    time.sleep(2)

    explosion_bombe(plateau, x, y)

    plateau[x][y] = 'J'

def explosion_bombe (plateau, x, y):
    def detruire_case (px, py):
        if plateau[px][py] == 'E':
            print("Un ennemi a été détruit à la position", (px, py))
        elif plateau[px][py] == 'B':
            print("Une brique cassable a été détruite à la position", (px, py))
        plateau[px][py] = '.'

    if x > 0:  # Haut
        detruire_case(x - 1, y)
    if x < len(plateau) - 1:  # Bas
        detruire_case(x + 1, y)
    if y > 0:  # Gauche
        detruire_case(x, y - 1)
    if y < len(plateau[0]) - 1:  # Droite
        detruire_case(x, y + 1)

    plateau[x][y] = '.'
    afficher_plateau(plateau)

# Boucle interactive pour déplacer le joueur
while True:
    afficher_plateau(plateau)  # Affiche le plateau actuel
    direction = input("\nEntrez une direction (haut, bas, gauche, droite), 'bombe' pour poser une bombe, ou 'q' pour quitter : ").lower()

    for i, ligne in enumerate(plateau):
        if 'J' in ligne:
            position_joueur = (i, ligne.index('J'))
            break

    if direction == 'q':  # Permet à l'utilisateur de quitter la boucle
        print("Fin du jeu.")
        break
    elif direction in ['haut', 'bas', 'gauche', 'droite']:
        deplacer_joueur(plateau, direction)  # Déplace le joueur dans la direction choisie
    elif direction == 'bombe' : 
        poser_bombe(plateau, position_joueur)
    else:
        print("Direction non valide. Veuillez entrer 'haut', 'bas', 'gauche', 'droite', 'bombe' ou 'q'.")
