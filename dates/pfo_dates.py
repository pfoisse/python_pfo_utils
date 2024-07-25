"""Module providing some functions to work with dates"""

from datetime import datetime
from datetime import timedelta

# ! --------------------------------------------
def set_date(year, month, day, hour=0, minute=0, second=0, microsecond=0):
    """"
    Crée une date au format datetime à partir des paramètres fournis.

    Args:
        year (int): année
        month (int): mois
        day (int): jour
        hour (int, optional): heure. Defaults to 0.
        minute (int, optional): minute. Defaults to 0.
        second (int, optional): seconde. Defaults to 0.
        microsecond (int, optional): milliseconde. Defaults to 0.

    Returns:
        datetime.datetime: la date créée

    Example:
        >>> set_date(2024, 10, 9, 11, 22, 33)
    """
    return datetime(year, month, day, hour, minute, second, microsecond)


# ! --------------------------------------------
def set_duree(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
    """
    Crée une durée au format datetime à partir des paramètres fournis.

    Args:
        weeks (int, optional): semaines. Defaults to 0.
        days (int, optional): jours. Defaults to 1.
        hours (int, optional): heures. Defaults to 0.
        minutes (int, optional): minutes. Defaults to 0.
        seconds (int, optional): secondes. Defaults to 0.
        milliseconds (int, optional): millisecondes. Defaults to 0.
        microseconds (int, optional): milliseconde. Defaults to 0.

    Returns:
        datetime.timedelta: la durée créée

    Example:
        >>> get_duree(weeks=2, days=3, hours=4, minutes=5, seconds=6, milliseconds=7, microseconds=8)
    """
  
    return timedelta(days, seconds, microseconds, milliseconds, minutes, hours, weeks)

# ! --------------------------------------------
def get_current_date():
    """"
    Crée une date au format datetime à partir de la date courante.

    Args:

    Returns:
        datetime.datetime: la date créée

    Example:
        >>> get_current_date()
    """
    return datetime.now()
    

# ! --------------------------------------------
def get_all_data_from_date(date_string):
    """
    Extrait et retourne toutes les données pertinentes à partir d'une date donnée au format datetime.

    Args:
        date_string (str): Une chaîne de caractères représentant une date au format 'AAAA-MM-JJ'.

    Returns:
        dict: Un dictionnaire contenant les informations suivantes :
            - date_complete (str): La chaîne de date d'origine.
            - date (datetime.date): L'objet date extrait de la chaîne.
            - annee (int): L'année de la date.
            - mois (int): Le mois de la date.
            - jour (int): Le jour de la date.
            - numero_jour_semaine (int): Le jour de la semaine (1-7, lundi=1).
            - jour_semaine (str): Le jour de la semaine sous forme de chaîne de caractères (par exemple, 'Lun', 'Mar', ...).
            - numero_semaine (int): Le numéro de semaine de l'année.
            - heure (int): L'heure de la date.
            - minute (int): La minute de la date.
            - second (int): La seconde de la date.
            - millisecond (int): La milliseconde de la date.

    Exemple:
        >>> obtenir_toutes_les_donnees_a_partir_de_date('2029-05-28')
    """

    # intialiser un dictionnaire vide pour mettre kles resultats
    d = {}

    # mettre les valeurs dans le ditionnaire qui contiendra les resultats
    
    d['date_complete'] = date_string
    d['date'] = date_string.date()

    d['annee'] = int(date_string.year)
    d['mois'] = int(date_string.month)
    d['jour'] = int(date_string.day)

    d['numero_jour_semaine'] = int(date_string.isoweekday())

    if d['numero_jour_semaine'] == 1:
        d['jour_semaine'] = 'Lun'
    if d['numero_jour_semaine'] == 2:
        d['jour_semaine'] = 'Mar'
    if d['numero_jour_semaine'] == 3:
        d['jour_semaine'] = 'Mer'
    if d['numero_jour_semaine'] == 4:
        d['jour_semaine'] = 'Jeu'
    if d['numero_jour_semaine'] == 5:
        d['jour_semaine'] = 'Ven'
    if d['numero_jour_semaine'] == 6:
        d['jour_semaine'] = 'Sam'
    if d['numero_jour_semaine'] == 7:
        d['jour_semaine'] = 'Dim'

    tuple = date_string.isocalendar() # Renvoie un tuple de 3 éléments (année, numéro de semaine, jour de la semaine).
    d['numero_semaine'] = int(tuple[1]) # Renvoie le numéro de semaine

    d['heure'] = int(date_string.hour)
    d['minute'] = int(date_string.minute)
    d['second'] = int(date_string.second)
    d['millisecond'] = date_string.microsecond

    return d

# ! --------------------------------------------
def convert_string_to_datetime(date_string):
    """"
    Convertit une chaîne de caractères en date au format datetime.

    Args:
        date_string (str): Une chaîne de caractères représentant une date au format 'AAAA-MM-JJ'.

    Returns:
        datetime.datetime: L'objet datetime créé à partir de la chaîne.

    Example:
        >>> convert_string_to_datetime('2029-05-28')
    """
    return datetime.strptime(date_string, '%Y-%m-%d')

    