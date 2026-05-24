# trabalho-IA

# Trabalho de Inteligência Artificial

## Classificação Supervisionada utilizando Python e R na base Iris Dataset

Projeto desenvolvido para a disciplina de Inteligência Artificial utilizando algoritmos de classificação supervisionada.


# Objetivo

Aplicar algoritmos de Machine Learning para classificação das espécies da base Iris Dataset utilizando Python e R.


# Algoritmos Utilizados

- Naive Bayes
- Árvore de Decisão
- Random Forest


# Tecnologias Utilizadas

## Python
- pandas
- scikit-learn
- matplotlib
- seaborn

## R
- caret
- randomForest
- rpart
- e1071


# Dataset

Foi utilizada a Iris Dataset, uma das bases mais conhecidas da área de Machine Learning.

A base contém:
- 150 registros;
- 3 espécies de flores;
- 4 atributos numéricos.


# Métricas Utilizadas

- Acurácia
- Precisão
- Recall
- F1-score
- Matriz de confusão


# Resultados

Os algoritmos apresentaram excelente desempenho na classificação supervisionada da base Iris Dataset.

## Python
- Naive Bayes: ~97,7%
- Árvore de Decisão: 100%
- Random Forest: 100%

## R
- Resultados superiores a 95% de acurácia.

# Integrantes
- Caroline Holanda Lima
- Ana Carolina
-  - Débora Rezende Valeriano
- Davi Maia de figueiredo
-  Davi Aquiles

  ---

# Como Executar o Projeto

## Python

### Instalar dependências

```bash
pip install pandas scikit-learn matplotlib seaborn
```

### Executar

```bash
python python/main.py
```

---

## R

### Instalar pacotes

```r
install.packages("e1071")
install.packages("randomForest")
install.packages("rpart")
install.packages("caret")
```

### Executar

Abra o arquivo:

```text
r/main.R
```

E execute no RStudio utilizando:

```r
source("main.R")
```

---

# Ferramentas Utilizadas

- Visual Studio Code
- RStudio
- GitHub

---

# Observações

O projeto utiliza a base Iris Dataset para classificação supervisionada utilizando algoritmos clássicos de Machine Learning.

Todos os algoritmos foram implementados em Python e R para fins de comparação de desempenho e aprendizado acadêmico.
