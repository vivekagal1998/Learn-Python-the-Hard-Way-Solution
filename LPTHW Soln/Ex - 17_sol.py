#!/usr/bin/env python3
import fileinput

with fileinput.FileInput("just.txt", inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace('import', 'importedfswf'), end='')


with open("just.txt") as file:
	filedata = file.read()

filedata = filedata.replace('copying','copied')

with open('just.txt', 'w') as file:
	file.write(filedata) 