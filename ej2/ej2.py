def fpp6d(num): #FloatingPointPrecision 6 Digits
	return ("{0:.6f}".format(num))

def conseguirInput():
	N =  int(raw_input())
	numeros = (map(lambda x: int(x), raw_input().split(" ")))
	return numeros
	
def listMergeSort(l):
	indexItererativeListMergeSort(l, 0, len(l))


def indexItererativeListMergeSort(l, start, end):
	distance = end - start
	if distance > 1:
		cutting_point = start + (distance / 2)
		indexItererativeListMergeSort(l, start, cutting_point)
		indexItererativeListMergeSort(l, cutting_point, end)

		indexIter = [start, cutting_point]
		tmp = []
		while indexIter[0] < cutting_point or indexIter[1] < end:
			
			if indexIter[0] == cutting_point:
				next_step = 1

			elif indexIter[1] == end:
				next_step = 0

			elif l[indexIter[1]] < l[indexIter[0]]:
				next_step = 1

			else:
				next_step = 0

			tmp.append(l[indexIter[next_step]])
			indexIter[next_step] += 1

		for x in range(start,end):
			l[x] = tmp[x - start]


def generarListaDeAparicionesRestantesInvertida(l): #l debe estar ordenado
	repetidos = []
	repetidos.append(1)
	p = 1

	for x in range(0, len(l) - 1):
		y = (len(l) - 2) - x

		if l[y] == l[y + 1]:
			p +=1
		else:
			p = 1 
		repetidos.append(p)

	return repetidos


def calcularEsperanza(l):
	listMergeSort(l)
	listaAparicionesRestantes = generarListaDeAparicionesRestantesInvertida(l)
	return bottomUpCalcularEsperanza(listaAparicionesRestantes,0,0)


def bottomUpCalcularEsperanza(l, next_cuerpo_precalculado, current_pos):

	cantidad_apariciones_elemento = l[current_pos]
	cantidad_total_de_elementos = current_pos + 1

	p_exito = cantidad_apariciones_elemento * (1.0)/cantidad_total_de_elementos
	p_fracaso = (1 - p_exito)
	
	cola = (1/p_exito)
	
	valor_esperanza = (next_cuerpo_precalculado) + cola
	valor_esperanza_print = fpp6d(valor_esperanza)
	
	current_pos+= 1	
	if current_pos < len(l):
		next_cuerpo_precalculado += cola * p_fracaso		
		valor_esperanza_print = bottomUpCalcularEsperanza(l, next_cuerpo_precalculado,current_pos) 
		
	
	return valor_esperanza_print


numeros =  conseguirInput()
print calcularEsperanza(numeros)
