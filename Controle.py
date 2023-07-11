from BancoDados import BancoDados
from ProdutoUnitario import ProdutoUnitario
from ProdutoPeso import ProdutoPeso
from Usuario import Usuario



class Controle:
  def __init__(self):
    self.__appOpen = True

  def addProduto(self):
    pass

  def verProduto(self):
    pass

  def cadastroUsuario(self):
    print("\nCadastro usuário\n")
    nome = input("Nome: ")
    senha = input("Senha: ")
    usuario = Usuario(nome, senha)
    db.addUsuario(usuario)
    print("\nUsuário cadastro")

  def loginUsuario(self):
    login = False

    print("\nLogin usuário\n")
    nome = input("Nome: ")
    senha = input("Senha: ")
    
    usuarios = db.getUsuarios()

    for i in usuarios:
      if i.getNome() == nome:
        if i.getSenha() == senha:
          i.changeLogin()
          usuarioLogado = i
          login = True
          return usuarioLogado
    
    while not login:
      print("\nNome ou senha incorretos")
      nome = input("Nome: ")
      senha = input("Senha: ")
    
      usuarios = db.getUsuarios()

      for i in usuarios:
        if i.getNome() == nome:
          if i.getSenha() == senha:
            i.changeLogin()
            usuarioLogado = i
            login = True
            return usuarioLogado
      
  def changeAppOpen(self):
    if self.__appOpen == True:
      self.__appOpen = False
    else:
      self.__appOpen = True

  def getAppOpen(self):
    return self.__appOpen


control = Controle()
db = BancoDados()
login = False

print("\nSISTEMA DE MERCADO")

while control.getAppOpen():
  opc = input("\n1)Cadastrar\n2)Login\n3)Fechar\nOpção: ")
  
  while opc != '1' and opc != '2' and opc != '3':
    print("\nOpção inválida, tente novamente")
    opc = input("1)Cadastrar\n2)Login\n3)Fechar\nOpção: ")

  if opc == '1':
    control.cadastroUsuario()

  elif opc == '2':
    usuarioLogado = control.loginUsuario()
    login = True

  else:
    control.changeAppOpen()

  while login and control.getAppOpen():
    print("\nPerfil Usuário")
    opc = input("\n1)Adicionar produto ao carrinho\n2)Ver carrinho\n3)Deslogar\n4)Fechar App\nOpção: ")

    while opc != '1' and opc != '2' and opc != '3' and opc != '4':
      print("\nOpção inválida, tente novamente")
      opc = input("1)Adicionar produto ao carrinho\n2)Ver carrinho\n3)Deslogar\n4)Fechar App\nOpção: ")

    if opc == '1':
      print("\nAdicionar produto")
      tipo = input("\n1)Unitario\n2)Peso\nTipo: ")
      
      while tipo != '1' and tipo != '2':
        print("\nOpção inválida, tente novamente")
        tipo = input("1)Unitario\n2)Peso\nTipo: ")

      nome = input("\nNome produto: ")
      valor = input("Valor unitário ou kg: ")
      quantidade = input("Quantidade unitário ou kg: ")

      if tipo == '1':
        produto = ProdutoUnitario(nome, valor, quantidade)
        usuarioLogado.addProduto(produto)

      else:
        produto = ProdutoPeso(nome, valor, quantidade)
        usuarioLogado.addProduto(produto)

    elif opc == '2':
      carrinho = usuarioLogado.getCarrinho()
      
      if len(carrinho) == 0:
        print("\nNão há produtos")
      else:
        for i in carrinho:
          print("\nNome: ",i.getNome())
          print("Valor: ",i.getValor())
          print("Quantidade: ",i.getQuantidade())

    elif opc == '3':
      usuarioLogado.changeLogin()
      login = False

    else:
      control.changeAppOpen()