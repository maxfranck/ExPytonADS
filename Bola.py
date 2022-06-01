class Bola:
    def __init__(self, color=None, circunf=0, material=None):
        self.color = color
        self.circunf = circunf
        self.material = material

    def trocaCor(self):
        troca = input(f"Deseja mudar a cor atual {self.color}? [s/n]")
        troca = troca[0].lower()

        if troca == "s":
            nova_cor = input("\n> Nova Cor: ")
            self.color = nova_cor
        else:
            print(f"Ok, a cor continua {self.color}")

    def mostraCor(self):
        print(f"\nA cor atual é {self.color}")

def main():
    bola01 = Bola("branca", 5, "couro")

    while True:
        bola01.mostraCor()
        bola01.trocaCor()

        continuar = input("Continuar? [s/n]")
        continuar = continuar[0].lower()
        if continuar == "n":
            break

    bola01.mostraCor()

main()