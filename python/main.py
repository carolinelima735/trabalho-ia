import pandas as pd

from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import GaussianNB

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

# =====================
# BASE IRIS
# =====================

iris = load_iris()

X = iris.data

y = iris.target

# =====================
# DIVISÃO
# =====================

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# =====================
# FUNÇÃO MÉTRICAS
# =====================

def avaliar(nome, y_real, y_pred):

    print(f"\n===== {nome} =====")

    print(
        "Acurácia:",
        accuracy_score(y_real, y_pred)
    )

    print(
        "Precisão:",
        precision_score(
            y_real,
            y_pred,
            average='weighted'
        )
    )

    print(
        "Recall:",
        recall_score(
            y_real,
            y_pred,
            average='weighted'
        )
    )

    print(
        "F1:",
        f1_score(
            y_real,
            y_pred,
            average='weighted'
        )
    )

    print("\nMatriz de Confusão:")

    print(
        confusion_matrix(
            y_real,
            y_pred
        )
    )

# =====================
# NAIVE BAYES
# =====================

modelo_nb = GaussianNB()

modelo_nb.fit(
    X_treino,
    y_treino
)

pred_nb = modelo_nb.predict(
    X_teste
)

avaliar(
    "Naive Bayes",
    y_teste,
    pred_nb
)

# =====================
# ÁRVORE
# =====================

modelo_dt = DecisionTreeClassifier(
    random_state=42
)

modelo_dt.fit(
    X_treino,
    y_treino
)

pred_dt = modelo_dt.predict(
    X_teste
)

avaliar(
    "Árvore de Decisão",
    y_teste,
    pred_dt
)

# =====================
# RANDOM FOREST
# =====================

modelo_rf = RandomForestClassifier(
    random_state=42
)

modelo_rf.fit(
    X_treino,
    y_treino
)

pred_rf = modelo_rf.predict(
    X_teste
)

avaliar(
    "Random Forest",
    y_teste,
    pred_rf
)