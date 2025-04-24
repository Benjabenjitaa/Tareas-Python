# Benjamin Pizarro Garcia
import itertools

def es_solucion_valida(piramide):
    for i in range(len(piramide) - 1):
        for j in range(len(piramide[i])):
            if abs(piramide[i][j] - piramide[i + 1][j]) > 3 or abs(piramide[i][j] - piramide[i + 1][j + 1]) > 3:
                return False
            return True

numeros = [1, 2, 3, 4, 5, 6]
soluciones = []

for permutacion in itertools.permutations(numeros):
    piramide = [[permutacion[0]],
               [permutacion[1], permutacion[2]],
               [permutacion[3], permutacion[4], permutacion[5]]]
    if piramide[0][0] == 3 and es_solucion_valida(piramide):
        soluciones.append(piramide)
        print('Soluciones')
        for solucion in soluciones:
            print(solucion)
    
print(len(soluciones))