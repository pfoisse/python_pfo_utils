
# ! --------------------------------------------
def printd(dico):
    """
    Afficher le contenu d un dictionnaire de facon claire et formatée

    Args:
        dico (dictionaire): nom du dictionnaire

    Returns:
        affiche le contenu du dictionnaire

    Example:
        
    """

    for item in dico:
        key = item
        value = dico[key]
        print(key)
        print('>', value)
        print()