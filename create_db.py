from database import Base,engine
from models import cnaecalculo, Lancamento

print("Creating database ....")

Base.metadata.create_all(engine)