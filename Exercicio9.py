import funcoes

print('Exercício 09 - Calculadora de descontos')
print('=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~')

desconto = float(input('Digite a porcentagem de desconto: '))
valor = float(input('Digite o valor da compra: '))

print(f'Preço final com desconto: {funcoes.valor_descontado(valor, desconto)}')
