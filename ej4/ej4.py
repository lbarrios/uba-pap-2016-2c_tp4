#!/usr/bin/env python

#UTILITY
def conseguirInput():
	global N
	global permutaciones,vistas
	N =  int(raw_input())
	permutaciones = (map(lambda x: int(x) - 1, raw_input().split(" ")))
	vistas = [False for x in permutaciones]

#MAIN
def calcularCiclos():
	global permutaciones, vistas, ciclos
	ciclos = []
	for x in range(0,N):
		if not vistas[x]:
			x2 = x
			i = 0
			while not vistas[x2]:
				i = i + 1
				vistas[x2] = True
				x2 = permutaciones[x2]
			ciclos.append(i)

def calcularTorneosPosibles():
	global ciclos
	valor = 1

	#iteraciones dentro de un ciclo
	for x in ciclos:
		valor *= pow(2,x/2) * isOdd(x)

	#iteraciones entre dos ciclos
	for x in range(0, len(ciclos) -1):
		for y in range(x+1, len(ciclos)):
			valor *= pow(2, MCD(ciclos[x],ciclos[y]))

	return valor


def calcularTorneosPosiblesConModulo():
	LIMITE_MODULAR = pow(10,9) + 7
	return calcularTorneosPosibles() % LIMITE_MODULAR

#MATH
def MCD(a,b):
	if a==0:
		return b
	else:
		return MCD(b%a, a)

def isOdd(number):
	return (number%2)


# RUN!
conseguirInput()
calcularCiclos()
print calcularTorneosPosiblesConModulo()
