## Aula 6 Teorema de Bayes

O pensamento Bayesiano fornece uma abordagem probabilística para aprendizagem. 

As quantidades de interesse são reguladas por distribuições de probabilidade.

Distribuição de probabilidade: é uma função que descreve a probabilidade de uma variável aleatória assumir certos valores.

### Teorema de Bayes

$P(c|X)$ é chamada de *probabilidade a posteriori* de *c* porque ela reflete nossa confiaça que *c* se mantenha após termos observado o vetor de treinamento *X*.

$P(c|X)$ reflete a influência do vetor de treinamento *X*

Em contraste, a probabilidade *a priori P(c)* é independente de *X*

Geralmente queremos encontrar a classe mais provável $\displaystyle c \in C$, sendo fornecidos exemplos de treinamento *X*. Ou seja, a classe com o *máximo a posteriori (MAP)*

$\displaystyle c_{MAP} \equiv \argmax_{c \in C} P(c|X)$

$\displaystyle = \argmax_{c \in C} \frac{P(X|c)P(c)}{P(X)}$

$\displaystyle = \argmax_{c \in C} P(X|c)P(c)$

### Classificador Ótimo de Bayes

Limitações práticas

* Como estimar com confiança todas estas probabilidades condicionais?
  * conjunto de treinamento com muitas instãncias
  * conhecer a distribuição de probabilidade
* A probabilidade a priori calculada geralmente não reflete a população.

Quando utilizar?

* Disponibilidade de um conjunto de treinamento grande ou moderado
* os atributos que descrevem as instãncias forem condicionalmente independentes dada a classe.

Aplicações bem sucedidas

* Diagnóstico médico

classificação de documentos textuais

O classificador de Naïve Bayes é baseado na suposição simplificadopra de que os valores dos atributos são condicionalmente independentes dado o valor alvo.

Ou seja, a probabilidade de observar a conjunção de atributos $\displaystyle a_1,a_2,...,a_n|C_k = \prod_i P(a_i | c_j)$

Temos assim o classificador $\displaystyle ĉ_{NB} = \argmax_{c_j \in C}P(c_j)\prod_iP(a_i|c_j)$ onde $c_{NB}$ indica o valor alvor fornecido pelo algoritmo Naïve Bayes

### Resumo

**Aprendizagem**: os termos $P(c_j)$ e $P(a_i|c_j)$ são estimados baseado nas suas frequências no conjunto de treinamento

Estas probabilidades "aprendidas" são então utilizadas para classificar uma nova instância aplicando a equação vista anteriormente

```
Treinamento_Naive_Bayes(conjunto de exemplos)
    Para cada valor alvo (classe) cj
        P'(cj) estimar P(cj)
        Para cada valor de atributo ai de cada atributo a
            P'(ai|cj) estimar P(ai|cj)
```

$\displaystyle ĉ_{NB} = \argmax_{c_j \in C} P'(c_j)\prod_{a_i \in x}P'(a_i|c_j)$


É um algoritmo simples e não sofisticado, pois assume que os valores dos atributos são condicionalmente independentes

Se a condição é encontrada, ele fornece a classificação MAP, caso contrário, pode ainda fornecer bons resultados.