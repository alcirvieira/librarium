# Importação dos módulos do SQL Alchemy.
from sqlalchemy import (
    create_engine, Column, ForeignKey,
    Integer, String, Date, Text, Boolean, DateTime
)

# Importação do ORM (Object-Relational Mapping) do SQL Alchemy.
from sqlalchemy.orm import (
    declarative_base,
    relationship
)


# Importa a biblioteca para manipular o sistema operacional.
import os

# Realiza a configuração do banco de dados no SQLite 3.
database_path = os.environ.get('DATA_DIR', 'data')
engine = create_engine(f'sqlite:///data/librarium.db')

# Interpreta as classes de objetos como tabelas de banco de dados.
# Configuração do SQL Alchemy que transforma as classes em tabela.
Tabular = declarative_base()


# Define uma tabela para armazenar as informações do usuário.
class Usuario (Tabular):

    # Nome da tabela.
    __tablename__ = 'usuario'

    # Atributos da tabela.
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False) # Para ser obrigado a inserir o nome do usuário
    cpf = Column(String(14), unique=True, nullable=False)
    nascimento = Column(Date, nullable=False)
    endereco = Column(Text, nullable=False)
    telefone = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False)
    senha = Column(String(255), nullable=False)
    perfil = Column(String(20), nullable=False)
    ativo = Column(Boolean, default=True)

    # Relacionamento.
    emprestimo = relationship('Emprestimo', back_populates='usuario')

    # Método que exibe todas as informações registradas.
    def __repr__ (self):

        # String formatada.
        return f'Usuário: {self.nome}, {self.cpf}, {self.nascimento}, {self.telefone}, {self.perfil}, {self.email}'
    

# Define uma tabela para armazenar as informações do livro.
class Livro (Tabular):

    # Nome da tabela.
    __tablename__ = 'livro'

    # Atributos da tabela.
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), nullable=False)
    isbn = Column(String(25), unique=True, nullable=False)
    autor = Column(Text, nullable=False)    
    editora = Column(String(100), nullable=False)
    edicao = Column(String(15), nullable=True)
    volume = Column(Integer, nullable=True)
    genero_literario = Column(String(100), nullable=False)
    numero_paginas = Column(Integer, nullable=False)
    ano_publicacao = Column(Integer, nullable=False)
    exemplares = Column(Integer, nullable=False)
    ativo = Column(Boolean, default=True)

    # Relacionamento.
    emprestimo = relationship('Emprestimo', back_populates='livro')

    # Método que exibe todas as informações registradas.
    def __repr__ (self):

        # String formatada.
        return f'livro: {self.titulo}, {self.ISBN}, {self.autor}, {self.edicao}, {self.volume} '
    

# Define uma tablea para vincular um leitor.
class Emprestimo (Tabular):

    # Nome da tabela.
    __tablename__ = 'emprestimo'

    # Atributos.
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    id_livro = Column(Integer, ForeignKey('livro.id'), nullable=False)
    data_emprestimo = Column(DateTime, nullable=False)
    data_devolucao = Column(DateTime, nullable=False)
    status = Column(String(25), nullable=False)
    ativo = Column(Boolean, default=True)

    # Relacionamentos.
    usuario = relationship('Usuario', back_populates='emprestimo')
    livro = relationship('Livro', back_populates='emprestimo')

    # Método que exibe todas as informações registradas.
    def __repr__ (self):

        # String formatada.
        return f'Emprestimo: {self.id}, {Livro.titulo}, {Usuario.nome}, {self.data_emprestimo}, {self.data_devolucao}'
    
