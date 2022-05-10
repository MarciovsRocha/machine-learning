## Aprendizagem de máquina não supervisionada

### Tarefas principais

* Agrupamento
* Associação

### 

* Quando os dados ou amostras de um problema não estão rotulados
* Busca descobrir padrões nos dados
* Tarefa principal: 
  * Agrupamento: Consiste em descobrir grupos com as mesmas qualidades/atributos

### Motivação

* Rotulação automática
  * Rotular bases é uma tarefa de alto custo, demanda um especialista no problema
  * é comum não se ter conhecimento das classes do problema quando do planejamento de modelos preditivos
* Descobertas de padrões: utilizada na minaração de dados que busca transformar dados brutos em conhecimento
* Um agrupamento pode ser utilizando antes da classificação de um classificador
  * Dada uma base de dados não rotulada, pode-se utilizar a aprendizagem não-supervisionada para fazer uma pré-classificação, e então treinar um classificador de maneira supervisionada

### Agrupamento (Clustering)

Organização de objetos em grupos segundo algum critério de similaridade

#### O que é um cluster?

Uma coleção de objetos que são similares entre si e diferentes dos outros objetos pertencentes a outros clusters.

Encontrar clusters demanda uma medida de similaridade.

Usualmente utiliza-se uma distância, o que caracteriza a forma mais comum de agrupamento: Distance-Based Clustering

##### k-Means Clustering

É a técnica mais simples de aprendizagem não supervisionada e consiste basicamente nos seguintes passos:

* Fixar k-Centróides (ponto representacional de um Cluster) para cada grupo (Cluster)
* Associar cada indivídui ao centróide mais próximo
* Recalcular os centróides com base nos indivíduos classificados

Lógica do algoritmo:
1. Determinar Centróides
2. Atribuir cada objeto do grupo ao centróirde mais próximo
3. Recalcular os centróides
4. Repetir os passos 2&3 até que os centróides não estejam modificados

Medidas de Distância

* Euclidiana
* Manhattan
* Mahalanobis

Criérios de Otimização

* O problema consiste em encontrar os clusters que minimizam/maximizam um dado critério
* Alguns critérios de otimização
  * Soma dos erros quadrados
    * É o mais simples e usado critério de otimização em clustering, seja n o número de exemplos no cluster **Di** e **Mi** a média desses exemplos $\displaystyle M_i = \frac{1}{n_i}\sum_{x \in D_i}x$ a soma dos erros quadrados é definida $\displaystyle J_e=\sum^{c}_{i=1}\sum_ {x \in D_i}(x-m_i)^2$
  * Critérios de dispersão
  * Indice de silhueta

Critérios de Dispersão

* Vetor médio do cluster **i** $\displaystyle m_i=\frac{1}{n_i}\sum_{x \in D_i}x$
* Vetor médio total $\displaystyle m=\frac{1}{n}\sum_Dx$
* Dispersão do cluster **i** $\displaystyle S_i=\sum_{x \in D_i}(x-m_i)(x-m_i)^t$
* Within-cluster $\displaystyle S_w = \sum^{c}_{i=1}S_i$
* between-cluster $\displaystyle S_B = \sum^{c}_{i=1}n_i(m_i-m)(m_i-m)^t$

Índice Silhueta

Cada cluster é representado por uma silhueta. Nos mostra que instãncias se posicionam bem dentro do cluster e o tamanho de cada cluster

A silhueta é calculada para cada instãncia (i) conforme abaixo:

$S(i) = \frac{(b(i)-a(i))}{max(a(i),b(i))}$

Onde

* a(i) é a dissimilarirade média da instância i em relação a todas as outras instâncias do seu cluster
* b(i) é a dissimilaridade média da instância i em relação a todas as outras instâncias do cluster vizinho mais próximo

Varia de -1 a 1m sendo -1 Indesejável. Silhueta negativa significa que a distância média dos objetos para seu cluster é maior que a distância média para outros clusters
