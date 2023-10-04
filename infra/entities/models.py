from typing import List
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from infra.configs.base import Base
#Criamos uma classe filme herdando Base (declarative_base)
class Filme(Base):
    #Definimos o nome da tabela
    __tablename__ = 'filme'

    #Definimos os atributos e seus tipos de dados que serao criados na base
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    titulo: Mapped[str] = mapped_column(nullable=False)
    genero: Mapped[str] = mapped_column(nullable=False)
    ano: Mapped[int] = mapped_column(nullable=False)
    atores: Mapped[List["Ator"]] = relationship("Ator", cascade="all, delete", passive_deletes=False, lazy='joined')


    #Sobrescrevemos a funcao magica que ocorre para apresentacao dos dados do objeto desta classe
    def __repr__(self):
        return f'Filme [Titulo = `{self.titulo},Ano = {self.ano}] \n'


class Ator(Base):
    __tablename__ = 'atores'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    nascimento: Mapped[int] = mapped_column(nullable=False)
    filme_id: Mapped[int] = mapped_column(ForeignKey("filme.id", ondelete="CASCADE"))

    def __repr__(self):
        return f'Ator [Nome = `{self.nome},Nascimento = {self.nascimento}] \n'
