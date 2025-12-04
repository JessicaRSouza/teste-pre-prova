#!/usr/bin/env python3

import sys
try:
	file = sys.argv[1]
	FASTA = open(file, "r")
	for line in FASTA:
		line = line.rstrip()
		print(line)
except IndexError:
	print("Please provide a file name")
except IOError:
	print("Can't find file:" , file)
