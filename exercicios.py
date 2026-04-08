# Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
"""numeros: list = range(1,11)
for n in numeros:
  print(n ** 2)"""

# Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
"""linguagens: list = ["Python", "Java", "C++", "JavaScript"]
linguagens.remove('C++')
linguagens.append('Ruby')
print(linguagens)"""

# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
"""livro_dict: dict = {
  'titulo': 'a história de babarikows',
  'autor': 'horácio googoo',
  'ano': 1997
}
print(livro_dict)"""

# Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
"""frase: str = 'babarikows googoo'
dict_frase: dict = {}
for letra in frase:
  dict_frase[f'{letra}'] = frase.count(letra)
print(dict_frase)"""

# Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
"""lista_frutas: list = ["maçã", "banana", "cereja"]
dict_frutas: dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
total_geral: float = 0

for item in lista_frutas:
  for chave, valor in dict_frutas.items():
    if item == chave:
      total_item: float = valor * lista_frutas.count(item)
      print(f'Total de {item}: {total_item}')
      total_geral += total_item

print(f'Total geral: {total_geral}')"""

# Dada uma lista de emails, remover todos os duplicados.
"""emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails_unicos = []

for item in emails:
  if item not in emails_unicos:
    emails_unicos.append(item)

print(emails_unicos)"""

# Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
"""lista_idades = [22, 15, 30, 17, 18]
lista_maiores = []

for idade in lista_idades:
  if idade >= 18:
    lista_maiores.append(idade)

print(lista_maiores)"""

# Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
"""pessoas = [
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20},
    {"nome": "Alice", "idade": 30},
]

pessoas_ordenado =  sorted(pessoas, key=lambda x: x['nome'])

print(pessoas_ordenado)"""


# Dado um conjunto de números, calcular a média.
"""numeros = [10, 20, 30, 40, 50]
media_numeros = sum(numeros)/len(numeros)
print(media_numeros)"""


# Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
"""valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valores_pares = []
valores_impares = []

for num in valores:
  if num % 2 == 0:
    valores_pares.append(num)
  else:
    valores_impares.append(num)

print(f'Valores pares: {valores_pares}')
print(f'Valores ímpares: {valores_impares}')"""


# Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
"""produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

id_usuario = int(input('Digite um ID entre 1 e 3: '))

for i in range(len(produtos)):
  if id_usuario == produtos[i]['id']:
    novo_preco = int(input('Digite o novo preço: '))
    produtos[i]['preço'] = novo_preco
    print(produtos)"""

# Dados dois dicionários, fundi-los em um único dicionário.
"""dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}
dicionario3 = {}

dicionario3.update(dicionario1)
dicionario3.update(dicionario2)

print(dicionario3)"""

# Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
"""estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}
estoque_maior = {}

for produto, qtd in estoque.items():
  if qtd > 0:
    estoque_maior.update({produto: qtd})

print(estoque_maior)"""

# Dado um dicionário, criar listas separadas para suas chaves e valores.
"""dicionario = {"a": 1, "b": 2, "c": 3}
lista_chaves = []
lista_valores = []

for chave, valor in dicionario.items():
  lista_chaves.append(chave)
  lista_valores.append(valor)

print(lista_chaves)
print(lista_valores)"""

# Dada uma string, contar a frequência de cada caractere usando um dicionário.
texto = "engenharia de dados"
dict_texto = {}
for letra in texto:
  dict_texto[letra] = texto.count(letra)

print(dict_texto)