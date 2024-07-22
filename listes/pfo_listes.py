"""Module providing some functions to work with list"""

# ! --------------------------------------------
def printl(liste):
    """
    Affiche le contenu d'une liste de manière claire et formatée. 
    Cette fonction prend en argument une liste et affiche chaque élément de la liste 
    avec un numéro d'ordre.

    Args:
        liste (list): nom de la liste

    Returns:
        affiche le contenu de la liste

    Example:
    liste = ['a', 'b', 'c', 'd']
    printl(liste)

    Cela donnera :
    0
    > a

    1
    > b

    2
    > c

    3
    > d
        
    """

    i = 0

    for item in liste:

        print(i)
        print('>', item)
        print()

        i = i + 1
        