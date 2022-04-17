#Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas vezes cada letra do alfabeto aparece dentro do arquivo.
nome = input("Nome do arquivo: ")
arq = open(f"{nome}.txt", "r")
texto = arq.read()

#tratamento
texto = texto.lower()
texto = texto.replace(" ","")
texto = texto.replace("\n","")
texto = texto.replace(".","")
texto = texto.replace(",","")

alfabeto = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

print("No arquivo tem a seguinte quantidade de cada letras do alfabeto:")
for letra in alfabeto:
   print(f"{letra.upper()}: {texto.count(letra)}")
