import json

"""lista: list = ['Sapato', 39, 10.38, True]

produto_01: dict = {
  'nome': 'Sapato',
  'quantidade': 39,
  'preco': 10.38,
  'disponibilidade': True
}

produto_02: dict = {
  'nome': 'Televisao',
  'quantidade': 10,
  'preco': 70.38,
  'disponibilidade': False
}

carrinho: list = []
carrinho.append(produto_01)
carrinho.append(produto_02)

#print(carrinho)

carrinho_json = json.dumps(carrinho)
print(carrinho_json)"""


livro_01: dict = {
  'titulo': 'a história de babarikows',
  'autor': 'horácio googoo',
  'ano': 1997
}

livro_02: dict = {
  'titulo': 'a ascenção de klips',
  'autor': 'arruda cabriocárico',
  'ano': 1993
}

dict_livros: dict = {
    'livro_01': livro_01,
    'livro_02': livro_02
}

print(dict_livros['livro_01']['titulo'])