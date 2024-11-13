from affichage import afficher_plateau
from deplacement import deplacer_ennemi, deplacer_joueur, poser_bombe
from initialisation import initialisation_plateau
from variables_globales import score
import variables_globales
plateau = initialisation_plateau()
# Boucle permettant de déplacé le joueur
while True:
    afficher_plateau(plateau)  # Affiche le plateau actuel
    direction = input("\nEntrez la direction (haut, bas, gauche, droite) ou 'q' pour quitter : ").lower()

    for i, ligne in enumerate(plateau):
        if 'J' in ligne:
            position_joueur= (i, ligne.index('J'))
            break

    if direction == 'q':  # Permet à l'utilisateur de quitter la boucle
        print(f"Fin du jeu. votre score est de : {variables_globales.score}")
        break
    elif direction in ['haut', 'bas', 'gauche', 'droite']:
        deplacer_joueur(plateau, direction)  # Déplace le joueur dans la direction choisie
        deplacer_ennemi(plateau)
    elif direction == 'bombe':
        poser_bombe(plateau, position_joueur)
    else:
        print("Direction non valide. Veuillez entrer 'haut', 'bas', 'gauche', 'droite' ou 'q'.")
