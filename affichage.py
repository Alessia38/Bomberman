def afficher_plateau(plateau):
    """Affiche le plateau de jeu."""
    for ligne in plateau:
        print(' '.join(ligne))