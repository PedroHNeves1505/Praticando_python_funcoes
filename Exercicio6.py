import funcoes

print('Exercício 06 - Filtrando números pares')
print('=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~')

numeros = input('Digite números separando-os por espaço: ').split()
numeros_pares = funcoes.filtrando_numeros_pares(numeros)
print('Números pares:')
for numero in numeros_pares:
	print(numero)
