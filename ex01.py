# Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas linhas esse arquivo possui
nome = input("Nome do arquivo: ")
arq = open(f"{nome}.txt", "r")
texto = arq.readlines()

valor = 0
for t in texto:
    valor +=1

print(f"O arquivo tem {valor} linhas.")