class CuentaBancaria:
  # Parámetros
  def __init__(self, numero_cuenta, propietarios, balance):
    # Atributos 
    self.numero_cuenta = numero_cuenta
    self.propietarios = propietarios
    self.balance = balance

  # Método para depositar dinero en la cuenta
  def depositar(self, monto):
    self.balance += monto
    print(f"Se ha depositado {monto} en la cuenta {self.numero_cuenta}. El nuevo balance es {self.balance}.")

  # Método para retirar dinero de la cuenta
  def retirar(self, monto):
    if monto <= self.balance:
      self.balance -= monto
      print(f"Se ha retirado {monto} de la cuenta {self.numero_cuenta}. El nuevo balance es {self.balance}.")
    else:
      print(f"No hay suficiente balance para retirar {monto} de la cuenta {self.numero_cuenta}. El balance actual es {self.balance}.")

  # Método para aplicar una cuota de manejo del 2% sobre el balance de la cuenta
  def aplicar_cuota_manejo(self):
    cuota = self.balance * 0.02
    self.balance -= cuota
    print(f"Se ha aplicado una cuota de manejo de {cuota} a la cuenta {self.numero_cuenta}. El nuevo balance es {self.balance}.")

  # Método para mostrar los detalles de la cuenta por consola
  def mostrar_detalles(self):
    print(f"Número de cuenta: {self.numero_cuenta}")
    print(f"Propietarios: {self.propietarios}")
    print(f"Balance: {self.balance}")
