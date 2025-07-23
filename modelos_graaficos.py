# Importando bibliotecas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Exemplo de DataFrame - Substitua pelos seus dados
dados = {
    'Idade': [23, 45, 31, 54, 27, 19, 41, 33, 39, 50],
    'Altura': [1.70, 1.85, 1.65, 1.75, 1.60, 1.68, 1.72, 1.80, 1.73, 1.78],
    'Peso': [70, 85, 60, 78, 55, 65, 72, 80, 75, 82]
}
df = pd.DataFrame(dados)

# Gráfico 1: Dispersão entre Altura e Peso
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Altura', y='Peso', data=df)
plt.title('Gráfico de Dispersão: Altura x Peso', fontsize=14)
plt.xlabel('Altura (m)')
plt.ylabel('Peso (kg)')
plt.show()

# Gráfico 2: Boxplot para verificar outliers
plt.figure(figsize=(8, 6))
sns.boxplot(data=df)
plt.title('Boxplot das Variáveis', fontsize=14)
plt.show()

# Gráfico 3: Matriz de Correlação (Heatmap)
plt.figure(figsize=(6, 4))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', cbar=True, square=True)
plt.title('Matriz de Correlação', fontsize=14)
plt.show()

# Gráfico 4: Histograma para analisar a distribuição de Idade
plt.figure(figsize=(8, 6))
sns.histplot(df['Idade'], kde=True, color='royalblue')
plt.title('Distribuição de Idade', fontsize=14)
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.show()
