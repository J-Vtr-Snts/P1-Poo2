class Usuario:
  def __init__(self, nome, senha):
    self.__nome = nome
    self.__senha = senha
    self.__login = False
    self.__carrinho = []

  def getNome(self):
    return self.__nome

  def getSenha(self):
    return self.__senha

  def getCarrinho(self):
    return self.__carrinho

  def addProduto(self, produto):
    self.__carrinho.append(produto)

  def login(self):
    return self.__login

  def changeLogin(self):
    if self.__login == False:
      self.__login = True
    else:
      self.__login = False