import funcoes

print('Exercício 02 - Contando caracteres')
print('=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~')

palavra = input('Digite uma palavra: ')
qnt_caracteres = funcoes.contador_caracteres(palavra)
print(f'Essa palavra tem {qnt_caracteres} caracteres.')
