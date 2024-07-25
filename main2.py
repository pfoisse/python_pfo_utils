from dates.pfo_dates import set_date
from dates.pfo_dates import get_current_date
from dates.pfo_dates import get_all_data_from_date
from dates.pfo_dates import set_duree


a = set_date(2000, 1, 1, 0, 0, 0)
print(a)

a = get_current_date()
print(a)

b = get_all_data_from_date(a)
print(b)

duree = set_duree(days=5, seconds=1)
print(duree)
