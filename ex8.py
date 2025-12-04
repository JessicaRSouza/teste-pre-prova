#!/usr/bin/env python3

def validar_sequencia(sequencia):
	try:
		if not sequencia:
			raise ValueError("A sequência de DNA está vazia.")
		if not all(base in "ATCG" for base in sequencia):
			raise ValueError("A sequência contém caracteres inválidos.")

		comprimento = len(sequencia)

		gc_content = (sequencia.count('G') + sequencia.count('C')) / comprimento * 100

		return comprimento, gc_content

	except ValueError as ve:
		return f"Erro de valor: {ve}"
	except Exception as e:
		return f"Erro desconhecido: {e}"

sequencias = ["ATCGATCG","ATGCATGX","","ATCGATCGATCG","ATGCGTACG","ATGCB"]

resultados = {}

for i, seq in enumerate(sequencias):
	resultado = validar_sequencia(seq)
	resultados[f"Sequência {i+1}"] = resultado

print(resultados) 
