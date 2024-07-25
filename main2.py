import datetime

from dates.pfo_dates import set_date
from dates.pfo_dates import get_current_date
from dates.pfo_dates import get_all_data_from_date
from dates.pfo_dates import set_duree


a = set_date(2000, 1, 1, 0, 0, 0)
print(a)
print(type(a))

print()

a = get_current_date()
print(a)

print()

b = get_all_data_from_date(a)
print(b)

print()

d = set_duree(seconds=1)

print(a)
print(a+d)






