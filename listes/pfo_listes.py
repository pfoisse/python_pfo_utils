"""Module providing some functions to work with list"""

# ! --------------------------------------------
def printl(liste):
    """
    Afficher le contenu d une liste de facon claire et formatée

    Args:
        liste (list): nom de la liste

    Returns:
        affiche le contenu de la liste

    Example:
        
    """

    i = 0

    for item in liste:

        print(i)
        print('>', item)
        print()

        i = i + 1
        