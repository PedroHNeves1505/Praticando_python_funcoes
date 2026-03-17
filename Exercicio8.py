import funcoes

print('Exercício 08 - Calculadora com lambda')
print('=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

operacao = input('Escolha a operação (| + | - | * | / |): ')
if operacao == '+':
	print(funcoes.operacoes['soma'](num1, num2))
elif operacao == '-':
	print(funcoes.operacoes['sub'](num1, num2))
elif operacao == '*':
	print(funcoes.operacoes['mult'](num1, num2))
elif operacao == '/':
	print(funcoes.operacoes['div'](num1, num2))
else:
	print('Operação inexistente')
