#Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas letras são vogais e quantas são consoantes
nome = input("Nome do arquivo: ")
arq = open(f"{nome}.txt", "r")
texto = arq.read()

#tratamento
texto = texto.lower()
texto = texto.replace(" ","")
texto = texto.replace("\n","")
texto = texto.replace(".","")
texto = texto.replace(",","")

vogais = 0
consoantes = 0

for t in texto:
    if t in 'aeiou':
       vogais = vogais + 1
    else:
       consoantes = consoantes + 1

print(f"Esse arquivo tem {vogais} vogais e {consoantes} consoantes")
