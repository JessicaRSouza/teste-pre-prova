#!/usr/bin/env python3

culturas = {
	'Milho': [1200, 1300, 1250],
	'Soja': [1500, -1600, 1400],
	'Trigo': [1000, 1100, 1050]
}

resultados = {}

for cultura, rendimentos in culturas.items():
	try:
		if any(rendimento < 0 for rendimento in rendimentos):
			raise ValueError(f"Rendimento não pode ser negativo para {cultura}.")
		media_rendimento = sum(rendimentos) / len(rendimentos)
		resultados[cultura] = media_rendimento

	except ValueError as e:
		print(f"Erro ao processar {cultura}: {e}")
		resultados[cultura] = "Erro no cálculo"

	except Exception as e:
		print(f"Erro desconhecido ao processar {cultura}: {e}")
		resultados[cultura] = "Erro desconhecido"

print(resultados)
