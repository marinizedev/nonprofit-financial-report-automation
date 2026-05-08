import calendar
from datetime import date

def ultimo_dia_do_mes(ano, mes):
    ultimo_dia = calendar.monthrange(ano, mes)[1]
    return date(ano, mes, ultimo_dia)