#!/usr/bin/python

import random

SIZE = 20

# elements thath will be predicted or
# is in dataset
class Element:
    def __init__(self, label: str, pos: tuple):
        self.label = label
        self.pos = pos

# dataset with all elements
class Dataset:
    ds: list
    def __init__(self):
        self.ds = []
    def add_element(self, element: Element):
        self.ds.append(element)
    def imprimir(self):
        matriz = [['--     --' for j in range(SIZE)] for i in range(SIZE)]
        for element in self.ds:
            matriz[element.pos[0]][element.pos[1]] = '--' + element.label + '--'
        return matriz

# eleva o número ao quadrado
sqr = lambda x: x**2

# raiz quadrada de um número
sqrt = lambda x: x**0.5

# distancia euclidian
# - recebe duas tuplas (X,Y) e
# - retorna a distância euclidiana entre elas
def distancia_euclidiana(p: tuple, q: tuple):
    return sqrt(sqr(p[0]-q[0]) + sqr(p[1]-q[1]))

# retorna os k menores elementos da lista
# a lista contem elementos (str, float)
def menores_da_lista(k_menores: int, distancias: list):
    distancias.sort(key=lambda x: x[1])
    menores = distancias[:k_menores]
    return menores

# conta as instancias da label na lista
def conta_instancias(label: str, lst: list):
    contador = 0
    for e in lst:
        if label == lst[0]:
            contador+=1
    return contador

# retorna a label de maior ocorrencia
def maior_ocorrencia(lst: list):
    labels = []
    ocorrencias = []
    for e in lst:
        if e[0] not in labels:
            labels.append(e[0])
            ocorrencias.append(conta_instancias(e[0],lst))
    return labels[ocorrencias.index(max(ocorrencias))]

# prediz label de element de acordo com k vizinhos próximos do dataset
# - k: numero de vizinhos
# - dataset: dataset com instancias
# - element: elemento que sera predito
# - f_distance: funcao que calcula a distancia entre 2 pontos
def k_nearest_neghbors(k: int, dataset: Dataset, element: Element, f_distance = distancia_euclidiana):
#    distancias = []
#    for e in dataset.ds:
#        distancias.append((e.label,f_distance(element.pos,e.pos)))
# gera uma tupla (label,distancia)
    distancias = [(e.label,f_distance(element.pos,e.pos)) for e in dataset.ds]
    return maior_ocorrencia(menores_da_lista(k, distancias))

# populando o Dataset
def popular_dataset(labels: list, dataset: Dataset, X = [i for i in range(SIZE)], Y = [i for i in range(SIZE)]):
    for label in labels:
        random.shuffle(X)
        random.shuffle(Y)
        for i in range(10):
            dataset.add_element(Element(label,(X[i],Y[i])))

X = [i for i in range(SIZE)]
Y = [i for i in range(SIZE)]
dataset = Dataset()
popular_dataset(['alpha','beta','teta','omega'],dataset,X,Y)
# gerando um novo elemento aleatorio
random.shuffle(X)
random.shuffle(Y)
identify = Element('X',(X[int(SIZE/2)],Y[int(SIZE/2)]))

## visualizacao do dataset com o elemento a ser previsto
printable = dataset.imprimir()
printable[identify.pos[0]][identify.pos[1]] = identify.label
for row in printable:
    line=''
    for e in row:
        line+=e
    print(line)

# predizendo o elemento aleatorio
l = k_nearest_neghbors(3,dataset,identify)
print('\n\nO elemento é da classe: {}'.format(l))
