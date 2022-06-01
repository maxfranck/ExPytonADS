class Conta():
	def __init__ (self, numero, nome, saldo=0) :
		self.numero = numero
		self.nome = nome
		self.saldo = saldo

	def setNome (self, nome):
		self.nome = nome

	def deposito (self, valor):
		self.saldo += valor

	def saque (self, valor):
		if (self.saldo >= valor):
			self.saldo -= valor

f = Conta(335, "Alexsander", 500.0)
print(vars(f))
f.setNome
f.deposito(50)
print(vars(f))
f.saque(110)
print(vars(f))