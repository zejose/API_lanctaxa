from datetime import datetime

import random

x = random.randint(1,999999999)

print(x)


x = datetime.today()
print(x)

#xxxxxxxxxxxxxxxxxxxxxxxxx
import models
from main import db

indice = db.query(models.cnaecalculo).filter(models.cnaecalculo.ano=="2020",models.cnaecalculo.cnae=="13" ).first()
#db_tem=db.query(models.Lancamento).filter(models.Lancamento.cpf_cnpj == item.cpf_cnpj).first()
#items=db.query(models.Lancamento).all()
print(indice.indice)