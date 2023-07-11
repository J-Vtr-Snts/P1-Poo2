from Produto import Produto


class ProdutoPeso(Produto):
  def __init__(self, nome, valorKg, quantidadeKg):
    super().__init__(nome)
    self.__valorKg = valorKg
    self.__quantidadeKg = quantidadeKg

  def getNome(self):
    return super().getNome()

  def getValor(self):
    return self.__valorKg

  def getQuantidade(self):
    return self.__quantidadeKg

  def setValor(self, valorKg):
    self.__valorKg = valorKg

  def setQuantidade(self, quantidadeKg):
    self.__quantidadeKg = quantidadeKg