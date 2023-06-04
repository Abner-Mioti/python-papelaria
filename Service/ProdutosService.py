from Repositorio.ProdutosRepositorio import ProdutosRepositorio
from Entidade.Produtos import Produtos

class ProdutosService:
    def __init__(self):
        self.repositorio = ProdutosRepositorio()
    
    def getAll(self):
        return self.repositorio.getAll()

    def getById(self, idProduto):
        return self.repositorio.getById(idProduto)

    def criarProduto(self, nome, preço_venda, preço_compra, grupo, quantidade_em_estoque):
        produto = Produtos(nome=nome, preço_venda=preço_venda, preço_compra=preço_compra, grupo=grupo, quantidade_em_estoque=quantidade_em_estoque)
        self.repositorio.criarProduto(produto)

    def updateProduto(self, id_produto, nome, preço_venda, preço_compra, grupo, quantidade_em_estoque):
        produto = self.repositorio.getById(id_produto)
        produto.nome = nome
        produto.preço_venda = preço_venda
        produto.preço_compra = preço_compra
        produto.grupo = grupo
        produto.quantidade_em_estoque = quantidade_em_estoque
        self.repositorio.updateProduto(produto)

    def deleteProduto(self, idProduto):
        self.repositorio.deleteProduto(idProduto)