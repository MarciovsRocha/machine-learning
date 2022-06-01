# TDE 1

Alunos: Marcio Vinicius de Souza da Rocha
Turma: BCC Noturno 5º Período

---

## Resultados algoritmo kNN

### SKLearn

```
[53  0  0  0  1  0  0  0  0  0]
[ 0 55  0  0  0  0  0  0  0  0]
[ 0  0 53  0  0  0  0  0  0  0]
[ 0  0  0 55  0  0  0  0  0  0]
[ 0  0  0  0 53  0  0  1  0  0]
[ 0  0  0  0  0 54  0  0  0  1]
[ 0  1  0  0  0  0 53  0  0  0]
[ 0  0  0  0  0  0  0 54  0  0]
[ 0  2  0  1  0  0  0  1 48  0]
[ 0  0  0  0  1  0  0  0  0 53]
Score: 98,4%
```

### Marcio

```
[54  0  0  0  0  0  0  0  0  0]
[ 0 55  0  0  0  0  0  0  0  0]
[ 0  0 53  0  0  0  0  0  0  0]
[ 0  0  0 55  0  0  0  0  0  0]
[ 0  0  0  0 54  0  0  0  0  0]
[ 0  0  0  0  0 54  0  0  0  1]
[ 0  0  0  0  0  0 54  0  0  0]
[ 0  0  0  0  0  0  0 54  0  0]
[ 0  3  0  1  0  0  0  0 48  0]
[ 0  0  0  0  1  0  0  0  1 52]
Score: 98,7%
```

função utilizada para calcular a distância: $$\displaystyle\sqrt{\sum_{n=0}((p_{n}-q_{n})^2+ \dots +(p_{n}-q_{n})^2)}$$

sendo $P$ & $Q$ instâncias distintas, $n$ é o índice do atributo *(coluna)* tal que este 

função utilizada para calcular o **Score**: $$Score=\frac{acertos}{(acertos+erros)}$$
