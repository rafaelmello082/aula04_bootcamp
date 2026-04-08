lista_numeros: list = [40,50,60,70,0,-408593,1,50]

def ordenar_lista(numeros: list) -> list:
  nova_lista = numeros.copy()

  for i in range(len(nova_lista)):
    for j in range(i+1, len(nova_lista)):
      if nova_lista[i] > nova_lista[j]:
        nova_lista[i], nova_lista[j] = nova_lista[j], nova_lista[i]
  
  return nova_lista

nova_01 = ordenar_lista(lista_numeros)
print(nova_01)