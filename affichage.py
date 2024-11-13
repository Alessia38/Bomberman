import variables_globales

def afficher_plateau(plateau):
    """Affiche le plateau de jeu."""
    print(f"score :  {variables_globales.score}")
    for ligne in plateau:
        print(' '.join(ligne))
        