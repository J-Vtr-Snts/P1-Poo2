from Produto import Produto


class ProdutoUnitario(Produto):
  def __init__(self, nome, valorUnit, quantidadeUnit):
    super().__init__(nome)
    self.__valorUnit = valorUnit
    self.__quantidadeUnit = quantidadeUnit

  def getNome(self):
    return super().getNome()

  def getValor(self):
    return self.__valorUnit

  def getQuantidade(self):
    return self.__quantidadeUnit

  def setValor(self, valorUnit):
    self.__valorUnit = valorUnit

  def setQuantidade(self, quantidadeUnit):
    self.__quantidadeUnit = quantidadeUnit