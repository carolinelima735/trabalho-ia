library(caret)

library(e1071)

library(randomForest)

library(rpart)



# =====================
# BASE IRIS
# =====================

data(iris)

# =====================
# SEMENTE
# =====================

set.seed(42)

# =====================
# DIVISÃO
# =====================

amostra <- sample(
  1:nrow(iris),
  0.7 * nrow(iris)
)

treino <- iris[amostra, ]

teste <- iris[-amostra, ]

# =====================
# NAIVE BAYES
# =====================

modelo_nb <- naiveBayes(
  Species ~ .,
  data = treino
)

pred_nb <- predict(
  modelo_nb,
  teste
)

confusionMatrix(
  pred_nb,
  teste$Species
)

# =====================
# ÁRVORE
# =====================

modelo_dt <- rpart(
  Species ~ .,
  data = treino
)

pred_dt <- predict(
  modelo_dt,
  teste,
  type = "class"
)

confusionMatrix(
  pred_dt,
  teste$Species
)

# =====================
# RANDOM FOREST
# =====================

modelo_rf <- randomForest(
  Species ~ .,
  data = treino
)

pred_rf <- predict(
  modelo_rf,
  teste
)

confusionMatrix(
  pred_rf,
  teste$Species
)

