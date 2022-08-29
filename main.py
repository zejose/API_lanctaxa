import random

from datetime import datetime
from datetime import date

from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import Optional, List

from sqlalchemy import desc

from database import SessionLocal
import models
import calculo_taxa
from calculo_taxa import anos_devidos_ai


app = FastAPI()

class Lancamento1(BaseModel): #serializer
    id:int
    cpf_cnpj:str
    nome:str
    endereco:str
    cidade:str
    estado:str
    cep:str
    valor_lancado:float
    cnae:str
    status_pagamento:str
    email:str

    class Config:
        orm_mode=True

class Lancamento(BaseModel): #serializer
    id:int
    cpf_cnpj:str
    nome:str
    endereco:str
    cidade:str
    estado:str
    cep:str
    data_inicio: Optional[date] = date.today()
    cnae:str
    area_utilizada:float
    status_pagamento:str
    email:str

    class Config:
        orm_mode=True

class V_lancamento(BaseModel): #serializer
    cpf_cnpj:str
    nome:str
    endereco:str
    cidade:str
    estado:str
    cep:str
    cnae: str
    valor_lancado:float
    n_sislanca:int

    class Config:
        orm_mode=True




db = SessionLocal()


@app.get('/items', response_model=List[V_lancamento], status_code=200)
def get_all_items():
    items = db.query(models.Lancamento).all()

    return items


@app.get('/item/{item_id}', response_model=Lancamento, status_code=status.HTTP_200_OK)
def get_an_item(item_id: int):
    item = db.query(models.Lancamento).filter(models.Lancamento.id == item_id).first()
    return item


@app.post('/items', response_model=Lancamento,
          status_code=status.HTTP_201_CREATED)
def create_an_item(item: Lancamento):
    db_item = db.query(models.Lancamento).filter(models.Lancamento.nome == item.nome).first()


    if db_item is not None:
        raise HTTPException(status_code=400, detail="Item already exists")

    ano_taxa = (item.data_inicio)
    ano_ini = int(ano_taxa.strftime('%Y'))
    data_inicial, anos_cobranca = anos_devidos_ai(item.data_inicio, datetime.today())
    print(data_inicial)
    print(ano_ini)
    print(ano_taxa)
    print(ano_ini)
    print(anos_cobranca)

    n_declaracao_registro = db.query(models.Lancamento).order_by(models.Lancamento.id.desc()).first()
    n_declaracao = (n_declaracao_registro.n_declaracao) + 1
    print(n_declaracao)
    print('xxxxxxxxxxxxssssssssssssssssssssssxxxxxxxxxxxx')


    for anos in anos_cobranca:

        new_item = models.Lancamento(

            cpf_cnpj=item.cpf_cnpj,
            nome=item.nome,
            n_declaracao=n_declaracao,
            endereco=item.endereco,
            cidade=item.cidade,
            estado=item.estado,
            cep=item.cep,
            data_inicio=item.data_inicio,
            cnae=item.cnae,
            valor_lancado=200,
            area_utilizada=item.area_utilizada,
            status_pagamento=item.status_pagamento,
            n_sislanca=random.randint(1,999999999),
            email=item.email
        )

        db.add(new_item)
        db.commit()


    return new_item



''''
@app.put('/item/{item_id}', response_model=Lancamento, status_code=status.HTTP_200_OK)
def update_an_item(item_id: int, item: Lancamento):
    item_to_update = db.query(models.Item).filter(models.Item.id == item_id).first()
    item_to_update.name = item.name
    item_to_update.price = item.price
    item_to_update.description = item.description
    item_to_update.on_offer = item.on_offer

    db.commit()

    return item_to_update


@app.delete('/item/{item_id}')
def delete_item(item_id: int):
    item_to_delete = db.query(models.Item).filter(models.Item.id == item_id).first()

    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")

    db.delete(item_to_delete)
    db.commit()

    return item_to_delete'''
