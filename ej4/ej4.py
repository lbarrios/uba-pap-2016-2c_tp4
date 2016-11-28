
def conseguirInput():
	global N
	global permutaciones,vistas
	N =  int(raw_input())
	permutaciones = (map(lambda x: int(x) - 1, raw_input().split(" ")))
	vistas = [False for x in permutaciones]


def isOdd(number):
	return (number%2)

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
	nciclos = len(ciclos)
	aristasGrafoCiclos = (nciclos * (nciclos - 1))/2
	valor = pow(2,aristasGrafoCiclos)
	for x in ciclos:
		valor *= pow(2,x/2) * isOdd(x)
	return valor

def calcularTorneosPosiblesConModulo():
	LIMITE_MODULAR = pow(10,9) + 7 
	return calcularTorneosPosibles() % LIMITE_MODULAR

conseguirInput()
calcularCiclos()
print calcularTorneosPosiblesConModulo()
