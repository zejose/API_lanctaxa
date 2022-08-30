
import calendar
import datetime
#import gspread
#import time
from decimal import *

import models



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


'''
def calcula_valor_taxa_tfe(ano_base, area_atividade=100, numero_cnae='01234'):
    cnae_usuario = str(numero_cnae)[0:2]
    print('cnae:', cnae_usuario)
    print('ano_base:', ano_base)
    ano_base = str(ano_base)

    tabela = db.query(models.cnaecalculo).filter_by(ano=ano_base, cnae=cnae_usuario).all()
    for dados in tabela:
        dado = dados.cnae
        dado1 = dados.cnae_extenso
        dado2 = dados.indice
        print(dado, dado1, dado2)

    valor_minimo = db.query(models.cnaecalculo).filter_by(ano=ano_base, cnae='VM1').first()
    print()

    valor_minimo_tfe = valor_minimo.indice
    valor_maximo = db.query(models.cnaecalculo).filter_by(ano=ano_base, cnae='VM2').first()
    valor_maximo_tfe = valor_maximo.indice
    print(valor_minimo_tfe,valor_maximo_tfe)


    cnae = dado
    #cnae = numero_cnae

    atividade_extenso = dado1
    #atividade_extenso = worksheet.cell(col_busca + 1, 2).value

    valor_indice_procurado = dado2
    #valor_indice_procurado = worksheet.cell(col_busca + 1, lin_busca + 1).value
    #print('valor do índice:', valor_indice_procurado)

    valor_final_taxa = float(valor_indice_procurado) * float(area_atividade)
    #print('valor da taxa:', valor_final_taxa)

    if valor_final_taxa < float(valor_minimo_tfe):
        valor_final_taxa = float(valor_minimo_tfe)
    #if valor_final_taxa < float(worksheet.cell(109, lin_busca + 1).value):
        #valor_final_taxa = float(worksheet.cell(109, lin_busca + 1).value)

    if valor_final_taxa > float(valor_maximo_tfe):
        valor_final_taxa = float(valor_maximo_tfe)
    #if valor_final_taxa > float(worksheet.cell(110, lin_busca + 1).value):
       # valor_final_taxa = float(worksheet.cell(110, lin_busca + 1).value)

    #return valor_final_taxa, cnae, atividade_extenso, valor_indice_procurado
    return valor_final_taxa'''

