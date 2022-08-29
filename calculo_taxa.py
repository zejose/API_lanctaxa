
import calendar
import datetime
#import gspread
#import time
from decimal import *


def anos_devidos_ai(data_inicio, data_final):

    data_termino_comparacao = int(data_final.strftime('%Y'))
    anos_cobranca = []
    d1 = data_inicio
    d2 = datetime.date.today()
    ano_atual = int(d2.strftime('%Y'))
    ano_ini = int(data_inicio.strftime('%Y'))
    years = ano_atual - ano_ini
    #print(ano_atual, ano_ini)

    data_termino_comparacao = int(data_final.strftime('%Y'))
    anos_cobranca = []
    d1 = data_inicio
    '''
    d2 = datetime.date.today()
    diff = d2 - d1
    days = diff.days
    years, days = days // 365, days % 365
    months, days = days // 30, days % 30
    '''
    if years > 4:
        data_bis = int(d2.strftime('%Y'))
        bisexto = calendar.leapdays(data_bis - 5, data_bis)
        data_inicial = d2 - datetime.timedelta(days=(1825 + (bisexto - 1)))
        years = 5
        data_str = int(data_inicial.strftime('%Y'))
        # print(days)
    else:
        data_inicial = d1
        data_str = int(data_inicial.strftime('%Y'))
    for anos in range(years + 1):
        if data_str <= data_termino_comparacao:
            anos_cobranca.append(data_str)  # anos de cobrança
            data_str = int(data_str) + 1

    return data_inicial, anos_cobranca