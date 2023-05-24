from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import LargeBinary
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Documento(Base):
    __tablename__ = "documento"

    id = Column(Integer, primary_key=True)
    identificador = Column(Integer, nullable=False)
    conteudo = Column(LargeBinary, nullable=False)
