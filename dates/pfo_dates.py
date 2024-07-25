"""Module providing some functions to work with dates"""

import datetime

# ! --------------------------------------------
def xxx():
    """"
    
    Args:

    Returns:
    
    Example:
    
    """

# ! --------------------------------------------
def set_date(year, month, day, hour=0, minute=0, second=0, microsecond=0):
    """"
    Crée une date à partir des paramètres fournis.

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
    return datetime.datetime(year, month, day, hour, minute, second, microsecond)


# ! --------------------------------------------
def set_duree(weeks=0, days=0, hours=0, minutes=0, seconds=0, milliseconds=0, microseconds=0):
    """
    Crée une durée à partir des paramètres fournis.

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
  
    return datetime.timedelta(weeks, days, hours, minutes, seconds, milliseconds, microseconds)


# ! --------------------------------------------
def get_current_date():
    """"
    Crée une date à partir de la date courante.

    Args:

    Returns:
        datetime.datetime: la date créée

    Example:
        >>> get_current_date()
    """
    return datetime.datetime.now()
    

# ! --------------------------------------------
def get_all_data_from_date(date_string):
    """"


    Args:

    Returns:
    
    Example:
    
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



    duree = datetime.timedelta(weeks = 1, days = 1, hours = 12, minutes = 5, seconds = 10, milliseconds = 345, microseconds = 456)

    print('Durée : ', duree)

    print('Date + Durée : ', date_string + duree)

    duree = datetime.timedelta(seconds = 1)


    print('Date : ', date_string)
    print('Durée : ', duree)
    print('Date + Durée : ', date_string + duree)

    return d


print('=====================================================')
print('=====================================================')
print('=====================================================')
print('=====================================================')


