# Importação das bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregando e visualizando os primeiros dados do dataset
df = pd.read_csv('data/Titanic-Dataset.csv')

# Mostra as primeiras 5 linhas do DataFrame
print(df.head())

# Mostra informações gerais sobre o DataFrame, incluindo o número de valores não nulos e os tipos de dados
print(df.info())

# Descrição estatística dos dados
print(df.describe())

# Distribuição das idades
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Distribuição das Idades dos Passageiros')
plt.xlabel('Idade')
plt.ylabel('Contagem')
plt.show()

# Proporção de sobreviventes
sobreviventes = df['Survived'].value_counts(normalize=True) * 100
print(f"Proporção de Sobreviventes: {sobreviventes}")

# Análise de Sobrevivência por Classe de Cabine
plt.figure(figsize=(10, 6))
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title('Sobrevivência por Classe de Cabine')
plt.xlabel('Classe de Cabine')
plt.ylabel('Número de Passageiros')
plt.legend(title='Sobreviveu', labels=['Não', 'Sim'])
plt.show()

# Análise de Sobrevivência por Sexo
plt.figure(figsize=(10, 6))
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title('Sobrevivência por Sexo')
plt.xlabel('Sexo')
plt.ylabel('Número de Passageiros')
plt.legend(title='Sobreviveu', labels=['Não', 'Sim'])
plt.show()
