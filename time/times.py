import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Dados fictícios
dados = {
    'TimeCasa': [1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    'TimeVisitante': [0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
    'RankingTimeCasa': [1, 2, 1, 1, 3, 2, 4, 1, 5, 1],
    'RankingTimeVisitante': [2, 1, 3, 4, 1, 3, 2, 5, 1, 4],
    'VitoriaTimeCasa': [1, 0, 1, 1, 0, 1, 0, 1, 0, 1]  # 1 se o time da casa ganhou, 0 caso contrário
}

# Criação do DataFrame
df = pd.DataFrame(dados)

# Definindo variáveis independentes (X) e a variável dependente (y)
X = df[['TimeCasa', 'TimeVisitante', 'RankingTimeCasa', 'RankingTimeVisitante']]
y = df['VitoriaTimeCasa']

# Dividindo os dados em conjuntos de treinamento e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=42)

# Criação do modelo de regressão logística
modelo = LogisticRegression()
modelo.fit(X_treino, y_treino)

# Fazendo previsões no conjunto de teste
y_pred = modelo.predict(X_teste)

# Calculando a acurácia do modelo
acuracia = accuracy_score(y_teste, y_pred)
print(f'Acurácia do modelo: {acuracia * 100:.2f}%')

# Prevendo a probabilidade de vitória do time da casa para um novo jogo
novo_jogo = np.array([[1, 0, 1, 2]])  # Exemplo: time da casa, não time visitante, ranking 1 para casa, ranking 2 para visitante
probabilidade_vitoria = modelo.predict_proba(novo_jogo)[0][1]  # Probabilidade do time da casa ganhar
print(f'Probabilidade do time da casa ganhar: {probabilidade_vitoria * 100:.2f}%')
