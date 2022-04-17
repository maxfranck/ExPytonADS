#Faça um programa que receba do usuario um arquivo texto. Crie outro arquivo texto contendo o texto do arquivo de entrada, mas com as vogais substituídas por ‘*’.
nome = input("Nome do arquivo: ")
arq_in = open(f"{nome}.txt", "r")
arq_out = open(f"{nome}(modificado).txt", "w")

for linha in arq_in:
	arq_out.write(linha.replace('a', '*').replace('e','*').replace('i','*').replace('o','*').replace('u','*'))

arq_in.close()
arq_out.close()