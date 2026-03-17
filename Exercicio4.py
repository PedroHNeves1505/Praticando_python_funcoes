import funcoes

print('Exercício 04 - Conversor de Tipos')
print('=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~')

continuar = True
telefones = []
while continuar:
	telefone = input('Digite os valores telefonicos: ')
	telefones.append(telefone)
	verificar = input('Deseja adicioanr mais números?: ')
	if verificar == 'sim':
		continuar = True
	else:
		continuar = False
int_telefones = funcoes.converter_tipos(telefones)
telefones = funcoes.converter_tipos(telefones)
print(funcoes.conferir_tipos(telefones))
for telefone in telefones:
	print(telefone)
