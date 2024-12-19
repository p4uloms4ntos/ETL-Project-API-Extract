from sqlalchemy.ext.declarative import declarative_base # Importa a classe declarative_base para criar uma classe base para a definição de tabelas.
from sqlalchemy import Column, Integer, Float, String, DateTime #  Importando os tipos de dados para a definição das colunas da tabela.
from datetime import datetime # Importa a classe datetime para manipular datas e horas.

# Cria uma classe base para a definição de tabelas (na versão 2.X do SQLAlchemy).
Base = declarative_base()

# Define a tabela no banco de dados. (BitcoinPreco)
class BitcoinPreco(Base):
    """Define a tabela no banco de dados."""
    __tablename__ = "bitcoin_precos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Float, nullable=False)
    criptomoeda = Column(String(50), nullable=False)  # até 50 caracteres
    moeda = Column(String(10), nullable=False)        # até 10 caracteres
    timestamp = Column(DateTime, default=datetime.now)