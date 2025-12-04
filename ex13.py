#!/usr/bin/env python3

# Tupla de cidades

cidades = ('Nova York', 'Londres', 'Tóquio', 'Sydney')



# Convertendo a tupla para lista para remover uma cidade

lista_cidades = list(cidades)

lista_cidades.remove('Tóquio')



# Lista de populações correspondentes às cidades

populacoes = [8.4, 8.9, 13.9, 5.3]



# Atualizando a população após a remoção de uma cidade

populacoes.pop(2)



# Convertendo a lista de populações atualizada de volta para uma tupla

populacoes_tupla = tuple(populacoes)


print(f"lista_cidades = {lista_cidades} e populacoes_tupla = {populacoes_tupla}")
