import funcoes

print('Exercício 07 - Juntando Listas de Produtos')
print('=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~')



produtos = input('Digite o nome dos produtos separando-os por vírgula: ').split(',')
valores = input('Digite o valor dos produtos separando-os por vírgula: ').split(',')

funcoes.juntando_listas_produtos(produtos, valores)
