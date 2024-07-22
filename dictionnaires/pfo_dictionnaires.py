"""Module providing some functions to work with dictionaires"""

# ! --------------------------------------------
def printd(dico):
    """
    Affiche le contenu d'un dictionnaire de manière claire et formatée. 
    Cette fonction prend en argument un dictionnaire 
    et affiche chaque couple clé-valeur du dictionnaire 
    avec le nom de la clé et la valeur associée.


    Args:
        dico (dictionaire): nom du dictionnaire

    Returns:
        affiche le contenu du dictionnaire

    Example:

    Voici comment utiliser cette fonction :

    dico = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    printd(dico)

    Cela donnera :

    a
    > 1

    b
    > 2

    c
    > 3

    d
    > 4
        
    """

    for item in dico:
        key = item
        value = dico[key]
        print(key)
        print('>', value)
        print()
