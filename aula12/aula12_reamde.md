## Redes Neurais 

* Regressor 
* Classificador

Redes Neurais Artificiais fornecem um método geral e prático para aprendizagem de funções de valor real e de valor discreto a partir de exemplos

Algoritmos como nackpropagation utilizam a descida do gradiente para ajustar os parãmetros das redes para melhor adaptar um conjunto de treinamento de pares (entrada-saída)

A aprendizagem de redes neurais é robusta a erros e ruídos nos dados de treinamento.

Modelo inspirado na aprendizagem de sistemas biológicos -> redes complexas de neurônios interconectados.

Entrada: neurônios de entrada (conforme a quantidade de atributos de entrada do problema)

Saída: neurônios de saída (em um problema de classificação normalmente um para cada classe do problema)

Camas Ocultas: quantidade e tamanho (números de neurônios) são definidos experimentalmente.

Rede neural elementar baseada em uma unidade chamada Perceptron criada por Rosenblatt em 1958.

Um Perceptron:
1. Recebe um vetor de entradas de valor real
2. Calcula uma combinação linear destas entradas
3. Fornece na saída: 
  - +1 
  - -1 

Onde cada elemento $w$ é uma constatne de valor real, ou peso, que determina a contribuição da entrada $x_i$ na saída do percepton

A aprendizagem do perceptron envolve a escolha dos valores dos pesos $w_0$ a $w_n$

A camada de entrada deve possuir uma unidade especial conhecida como *bias*, que é um termo constante que não depende de nenhum valor de entrada.

os pesos do perceptron são modificados a cada passo de acordo com a regra de treinamento do perceptron que modifica o peso $w_i$ associado a entrada $x_i$ de acordo com a regra

$w_i \leftarrow w_i+\Delta w_i$

onde 

$\Delta w_i \equiv \eta(t-o)x_i$

* $t$ é o valor alvo para o exemplo de treinamento
* $o$ é a saída gerada pelo perceptron 
* $\eta$ é uma constante pequena (0.1) chamada de taxa de aprendizagem
