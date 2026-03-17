

def calcula_idade(ano_nascimento:int ,ano_atual:int ):
	"""Calcula a idade baseada no ano de nascimento.

	Args:
		ano_nascimento: O ano em que a pessoa nasceu (ex: 1990).
		ano_atual: O ano de referência para o cálculo.

	Returns:
		A idade calculada em anos.

	Raises:
		ValueError: Se ano_nascimento maior que ano_atual
		ValueError: Se ano_nascimento ou ano_atual não for int
	"""
	return ano_atual - ano_nascimento


def contador_caracteres(palavra):
	"""Conta a quantidade de caracteres de uma palavra
	
	Args:
		palavra: palavra aleatoria que o usuário vai digitar
	
	Returns:
		quantidade de caracteres da palavra
	"""
	return len(palavra)


def saudacao_personalizada(horario: int):
	"""Muda a saudação dependendo do horario
	
	Args:
		horario: hora do dia
	
	Returns:
		saudação diferente dependendo do horario
	
	Raises:
		ValueError: Se horario não for int
	"""
	if horario < 12:
		return 'Bom dia!'
	elif 12 <= horario <= 18:
		return 'Boa tarde!'
	else:
		return 'Boa noite!'

def converter_tipos(telefones):
	""" Pega as strings da lista telefones e tranforma em inteiro
	
	Args:
		telefones: lista com as strings para transformar
	
	Returns:
		Lista de telefones com valores inteiros
	"""
	telefones_int = []
	for telefone in telefones:
		telefones_int.append(int(telefone))
	return telefones_int
	
def conferir_tipos(telefones):
	""" Confere os valores da lista telefones

	Args:
		telefones: lista com os valores int para conferir

	Returns:
		Se valores na lista telefones são inteiros ou não
	"""
	for telefone in telefones:
		if type(telefone) == int:
			return 'Todos os números foram convertidos corretamente!'
		else:
			return 'Os números não foram convertidos corretamente!'
		

def Calculando_total_vendas(valor_vendas):
	"""Calcula o valor total de vendas
	
	Args:
		valor_vendas: valor de todas as vendas realizadas
	
	Returns:
		Soma de todas as vendas realizadas
	
	Raises:
		ValueError: Se um valor no valor_vendas não for float
	"""
	vendas_total = 0
	for valor in valor_vendas:
		vendas_total = vendas_total + float(valor)
	return vendas_total

def filtrando_numeros_pares(numeros):
	"""Filtra números do usuário
	
	Args:
		numeros: números recebidos do usuário
	
	Returns:
		numeros pares dos numeros em numeros
	
	Raises:
		ValueError: Se um numero nos numeros não for float
	"""
	numeros_pares = []
	for numero in numeros:
		if float(numero) % 2 == 0:
			numeros_pares.append(numero)
		else:
			continue
	return numeros_pares

def juntando_listas_produtos(produtos, valores):
	""" Recebe as listas produtos e valores, as uni e imprime seus valores juntos
	
	Args:
		produtos: nome dos produtos
		valores: valor dos produtos
	
	Returns:
		nome do produto com seu valor
	"""
	for produto, valor in zip(produtos, valores):
		print(f"{produto.strip()}: {valor.strip()}")

"""
	Dicionario de operações aritméticas
	Funções feitas com funções lambda (a: float, b:float) --> float
"""
operacoes = {
	'soma': lambda a, b: a + b,
	'sub': lambda a, b: a - b,
	'mult': lambda a, b: a * b,
	'div': lambda a, b: a / b if b != 0 else float('nan')
}


valor_descontado = lambda valor, desconto: valor - (desconto / 100) * valor

def soma_recursiva(numero):
	soma = 0
	while numero > 0:
		soma = soma + numero
		numero -= 1
	return soma
