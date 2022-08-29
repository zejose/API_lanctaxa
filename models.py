
import datetime
from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String, Boolean, Integer, Column, Text, DateTime, Float

class Lancamento(Base):
    __tablename__='lancamento'
    id=Column(Integer,primary_key=True)
    n_declaracao=Column(Integer,nullable=True)
    nome=Column(String,nullable=True)
    cpf_cnpj=Column(String,nullable=True)
    data_inicio=Column(DateTime(datetime.date),nullable=True)
    endereco=Column(String,nullable=True)
    cidade=Column(String,nullable=True)
    estado=Column(String,nullable=True)
    cep=Column(String,nullable=True)
    cnae=Column(String,nullable=True)
    area_utilizada=Column(Float, nullable=True)
    valor_lancado=Column(Float,nullable=True)
    n_sislanca=Column(Integer,nullable=True )
    status_pagamento=Column(String,nullable=True)
    email=Column(String, nullable=True, unique=False)

    def __repr__(self):
        return f"<Lancamento nome={self.nome} valor_lancado={self.valor_lancado}>"

class cnaecalculo(Base):
    __tablename__ = 'cnae_calculo'
    id = Column(Integer, primary_key=True)
    ano = Column(Integer, nullable=False)
    cnae = Column(String, nullable=False)
    cnae_extenso = Column(String, nullable=False)
    indice = Column(String, nullable=False)

    def __init__(self, ano, cnae, cnae_extenso, indice):
        self.ano = ano
        self.cnae = cnae
        self.cnae_extenso = cnae_extenso
        self.indice = indice

    def __repr__(self):
        return f"<cnaecalculo ano={self.ano} cnae={self.cnae}>"