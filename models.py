from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

# Cria a conexão com o banco
db = create_engine("sqlite:///banco.db")

# Cria a base do banco de dados
Base = declarative_base()

# Criar as bases/tabelas do banco de dados

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id_usuario", Integer, primary_key=True, autoincrement=True)
    nome =  Column("nome", String)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, p_nome, p_email, p_senha, p_ativo=True, p_admin=False):
        self.nome = p_nome
        self.email = p_email
        self.senha = p_senha
        self.ativo = p_ativo
        self.admin = p_admin

class Pedido(Base):
    __tablename__ = "pedidos"

    # STATUS_PEDIDOS = (
    #     ("PENDENTE", "PENDENTE"),
    #     ("CANCELADO", "CANCELADO"),
    #     ("FINALIZADO", "FINALIZADO")
    # )

    id = Column("id_pedido", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String) # Pendente, cancelado e finalizado
    usuario = Column("usuario", ForeignKey("usuarios.id_usuario"))
    preco = Column("preco", Float)
    #itens = 

    def __init__(self, p_usuario, p_status="PENDENTE", p_preco=0):
        self.status = p_status
        self.usuario = p_usuario
        self.preco = p_preco

class ItensPedido(Base):
    __tablename__ = "itens_pedido"

    id = Column("id_item", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", String)
    preco_unitario = Column("preco_unitario", Float)
    pedido = Column("pedido", ForeignKey("pedidos.id_pedido"))

    def __init__(self, p_quantidade, p_sabor, p_tamanho, p_precounitario, p_pedido):
        self.quantidade = p_quantidade
        self.sabor = p_sabor
        self.tamanho = p_tamanho
        self.preco_unitario = p_precounitario
        self.pedido = p_pedido


# Executa a criação dos metadados do seu banco (cria efetivamente o banco de dados)
