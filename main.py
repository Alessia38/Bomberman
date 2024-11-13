from affichage import afficher_plateau
from deplacement import deplacer_ennemi, deplacer_joueur
from affichage import afficher_plateau
from initialisation import initialisation_plateau

def jeu():
    plateau = initialisation_plateau()
    # Boucle permettant de déplacé le joueur
    while True:
        afficher_plateau(plateau)  # Affiche le plateau actuel
        direction = input("\nEntrez la direction (haut, bas, gauche, droite) ou 'q' pour quitter : ").lower()

        if direction == 'q':  # Permet à l'utilisateur de quitter la boucle
            print("Fin du jeu.")
            break
        elif direction in ['haut', 'bas', 'gauche', 'droite']:
            deplacer_joueur(plateau, direction)  # Déplace le joueur dans la direction choisie
            deplacer_ennemi(plateau)
        else:
            print("Direction non valide. Veuillez entrer 'haut', 'bas', 'gauche', 'droite' ou 'q'.")

if __name__ == "__main__":
    jeu()