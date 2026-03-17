import funcoes

print('Exercício 01 - Calculando a idade pelo ano de nascimento')
print('=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~')

ano_nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))
idade = funcoes.calcula_idade(ano_nascimento, ano_atual)
print(f'A idade é {idade} anos')


