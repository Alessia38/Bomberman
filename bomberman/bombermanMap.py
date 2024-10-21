# Initialisation du tableau avec des ennemis (E) à des positions fixes
plateau = [
    ['.', '.', '.', '.', '.'],
    ['.', '.', 'E', '.', '.'],
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

    # Déplacer le joueur vers la nouvelle position
    plateau[x][y] = '.'  # Efface l'ancienne position
    plateau[nouveau_x][nouveau_y] = 'J'  # Place le joueur dans la nouvelle position


# Boucle interactive pour déplacer le joueur
while True:
    afficher_plateau(plateau)  # Affiche le plateau actuel
    direction = input("\nEntrez la direction (haut, bas, gauche, droite) ou 'q' pour quitter : ").lower()

    if direction == 'q':  # Permet à l'utilisateur de quitter la boucle
        print("Fin du jeu.")
        break
    elif direction in ['haut', 'bas', 'gauche', 'droite']:
        deplacer_joueur(plateau, direction)  # Déplace le joueur dans la direction choisie
    else:
        print("Direction non valide. Veuillez entrer 'haut', 'bas', 'gauche', 'droite' ou 'q'.")
