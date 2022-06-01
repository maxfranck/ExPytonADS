class Funcionario():
	def __init__ (self, nome, salario):
		self.nome = nome
		self.salario = salario

	def getNome(self):
		return self.nome

	def getSalario(self):
		return self.salario

Func = Funcionario("Alex",1200)
print("Nome",Func.getNome(),"Salario",Func.getSalario())