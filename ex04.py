#Faça um programa que receba do usuário um arquivo texto e um caracter. Mostre na tela quantas vezes aquele caractere ocorre dentro do arquivo.
nome = input("Nome do arquivo: ")
arq = open(f"{nome}.txt", "r")
texto = arq.read()

#tratamento
texto = texto.lower()
texto = texto.replace(" ","")
texto = texto.replace("\n","")
texto = texto.replace(".","")
texto = texto.replace(",","")

valor = input("Informe uma letra: ")
valor = valor.lower()
letra = 0

for t in texto:
    if t in valor:
       letra = letra + 1

print(f"A letra {valor} repete {letra} vezes nesse arquivo")
