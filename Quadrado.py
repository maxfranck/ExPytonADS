class Quadrado:
    def __init__(self, lado="0"):
        self.lado = lado

    @property
    def lado(self):
        return self.__lado

    @lado.setter
    def lado(self, valor):
        if valor.isdigit():
            self.__lado = valor
        else:
            print("O valor do lado deve ser apenas em numeros")

    def valorLado(self):
        print(f"\nO valor do lado é {self.__lado} cm")

    def mudarLado(self):
        novoLado = input(f"\nMudar lado de {self.__lado} cm para: ")
        self.lado = novoLado

    def calcArea(self):
        print(f"\nA área do quadrado é {float(self.__lado) * float(self.__lado):.2f} cm²")

    def __str__(self):
        return f"O quadrado possui {self.__lado} cm de lado e {float(self.__lado) * float(self.__lado):.2f} cm² de area"

def main():
    quadradoA = Quadrado()
    lado = input("Insira o valor do lado: ")
    quadradoA.lado = lado

    print(quadradoA)

    quadradoA.mudarLado()
    quadradoA.valorLado()
    quadradoA.calcArea()

main()