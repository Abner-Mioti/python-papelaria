import json
from Base.Base import Base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

class Produtos(Base):
    __tablename__ = 'produtos'

    id_produto = Column(Integer, primary_key=True)
    nome = Column(String)
    preço_venda = Column(Float)
    preço_compra = Column(Float)
    grupo = Column(String)
    quantidade_em_estoque = Column(Integer)

    vendas = relationship("Venda", back_populates="produtos")

    def to_dict(self):
        return {
            'id_produto': self.id_produto,
            'nome': self.nome,
            'preço_venda': self.preço_venda,
            'preço_compra': self.preço_compra,
            'grupo': self.grupo,
            'quantidade_em_estoque': self.quantidade_em_estoque
        }

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.to_dict(), indent=4)