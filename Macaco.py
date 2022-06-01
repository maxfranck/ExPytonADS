class Macaco():
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)

    def verBucho(self):
        print ("Bucho : ", self.bucho)

    def digerir (self):
        if (len(self.bucho)>0):
            self.bucho.pop(0)

m1 = Macaco ("Macaco 1")
m2 = Macaco ("Macaco 2")

m1.comer("Maçã")
m1.verBucho()

m1.comer("Banana")
m1.verBucho()

m1.comer("Abacaxi")
m1.verBucho()
m1.digerir()
m1.verBucho()

m2.comer("Maçã")
m2.comer("Banana")
m2.comer(m1)
m2.verBucho