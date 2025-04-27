import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Gerar dados simulados
np.random.seed(42)

produtos = ['Smartphone XYZ', 'Notebook Pro 14', 'TV 55" UltraHD', 'Fone Bluetooth', 
            'Geladeira FrostFree', 'Máquina de Lavar', 'Micro-ondas', 'Aspirador 3000']

categorias = {
    'Smartphone XYZ': 'Eletrônicos',
    'Notebook Pro 14': 'Eletrônicos',
    'TV 55" UltraHD': 'Eletrônicos',
    'Fone Bluetooth': 'Eletrônicos',
    'Geladeira FrostFree': 'Eletrodomésticos',
    'Máquina de Lavar': 'Eletrodomésticos',
    'Micro-ondas': 'Eletrodomésticos',
    'Aspirador 3000': 'Eletrodomésticos'
}

localizacoes = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Outras Cidades']

# Criar DataFrame
n = 200
dados = pd.DataFrame({
    'ID_Venda': np.arange(1, n+1),
    'Data': pd.date_range(start='2024-01-01', periods=n, freq='D'),
    'Produto': np.random.choice(produtos, n),
    'Quantidade': np.random.randint(1, 9, size=n),
    'Cliente_ID': np.random.randint(1000, 9999, size=n),
    'Localização': np.random.choice(localizacoes, n)
})

# Atribuir categorias
dados['Categoria'] = dados['Produto'].map(categorias)

# Atribuir preços (valores aleatórios realistas)
precos_base = {
    'Smartphone XYZ': 1500,
    'Notebook Pro 14': 4500,
    'TV 55" UltraHD': 2500,
    'Fone Bluetooth': 300,
    'Geladeira FrostFree': 3200,
    'Máquina de Lavar': 2800,
    'Micro-ondas': 800,
    'Aspirador 3000': 500
}

dados['Preço_Unitário'] = dados['Produto'].map(precos_base) + np.random.normal(0, 200, size=n).astype(int)

# Mostrar os primeiros registros
print(dados.head())

# -------------------------
# Plotagem dos gráficos
# -------------------------

# 1. Quantidade
plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)
sns.histplot(dados['Quantidade'], bins=8, kde=False)
plt.title('Histograma - Quantidade de Unidades Vendidas')

plt.subplot(1, 2, 2)
sns.boxplot(x=dados['Quantidade'])
plt.title('Boxplot - Quantidade de Unidades Vendidas')

plt.show()

# 2. Preço Unitário
plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)
sns.histplot(dados['Preço_Unitário'], bins=20, kde=False)
plt.title('Histograma - Preço Unitário')

plt.subplot(1, 2, 2)
sns.kdeplot(dados['Preço_Unitário'], shade=True)
plt.title('Curva de Densidade (Preço Unitário)')

plt.show()

# 3. Categoria
plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)
sns.countplot(x=dados['Categoria'])
plt.title('Contagem de Vendas por Categoria')

plt.subplot(1, 2, 2)
dados['Categoria'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, explode=(0.05, 0))
plt.title('Distribuição Percentual por Categoria')
plt.ylabel('')

plt.show()

# 4. Produto
top_produtos = dados['Produto'].value_counts().head(10)

plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)
top_produtos.plot(kind='bar')
plt.title('Top 10 Produtos Mais Vendidos')

plt.subplot(1, 2, 2)
acum = top_produtos.cumsum() / top_produtos.sum()
acum.plot(marker='o')
plt.axhline(0.8, color='red', linestyle='--')
plt.title('Gráfico de Pareto dos Produtos')
plt.ylabel('Fração acumulada')

plt.show()

# 5. Localização
plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)
sns.countplot(x=dados['Localização'])
plt.title('Quantidade de Vendas por Localização')

plt.subplot(1, 2, 2)
dados['Localização'].value_counts().plot(kind='barh', color='skyblue')
plt.title('Distribuição de Vendas por Localização')

plt.show()
