## MEU KNN DESENVOLVIDO
#!/usr/bin/python

# elements that will be predicted or
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


# eleva o número ao quadrado
sqr = lambda x: x**2

# raiz quadrada de um número
sqrt = lambda x: x**0.5


# distancia euclidian
# - recebe duas tuplas (X, Y, .., Z) e
# - retorna a distância euclidiana entre elas
def distancia_euclidiana(p: tuple, q: tuple):
    # as duas tuplas devem ter o mesmo número de atributos para que seja calculada corretamente
    if len(p) != len(q):
        return 0
    somatorio = 0
    index = 0
    while len(p) > index:
        somatorio += (sqr(p[index]-q[index]) + sqr(p[index]-q[index]))
        index += 1
    return sqrt(somatorio)


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
def k_nearest_neghbors(k: int, dataset: Dataset, element: Element, f_distance=distancia_euclidiana):
    distancias = [(e.label, f_distance(element.pos, e.pos)) for e in dataset.ds]
    return maior_ocorrencia(menores_da_lista(k, distancias))


# predizendo elementos sobre uma base
# retorna uma lista de labels preditas
# - elements_to_predict: lista de atributos
def predict_datasets(elements_to_predict, ds,k_neighbors: int = 3):
  preditos = []
  for e in elements_to_predict:
    preditos.append(k_nearest_neghbors(k_neighbors, ds, Element('', tuple(e))))
  return preditos

