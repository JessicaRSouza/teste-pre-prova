#!/usr/bin/env python3

with open('numeros.txt', 'r') as file:
	numeros = file.readlines()

soma = sum([int(num.strip()) for num in numeros])
media = soma / len(numeros)

with open('media.txt', 'w') as file:
	file.write(f'A média é: {media}')
