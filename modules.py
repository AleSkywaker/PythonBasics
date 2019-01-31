# propios modulos
# modulos de terceros
# modulos propios de python
import datetime

print(datetime.date.today())
#timedelta convierte minutos en horas
print(datetime.timedelta(minutes=70))

#otra forma de importarlo es 
from datetime import timedelta,date
# su uso cambiaria y seria directamente
print(timedelta(minutes=100))
print(date.today())