class BancoDados:
  def __init__(self) -> None:
    self.__usuarios = []

  def addUsuario(self, usuario):
    self.__usuarios.append(usuario)

  def getUsuarios(self):
    return self.__usuarios