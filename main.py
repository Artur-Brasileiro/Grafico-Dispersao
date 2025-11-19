import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# --- Leitura e limpeza básica ---
df = pd.read_csv('pressao_arterial.csv')
df.columns = df.columns.str.strip()

# converte colunas importantes para numérico
for col in ['idade', 'pressao_sistolica']:
    df[col] = (
        df[col]
        .astype(str)
        .str.strip()
        .str.replace(',', '.', regex=False)
    )
    df[col] = pd.to_numeric(df[col], errors='coerce')

df = df.dropna(subset=['idade', 'pressao_sistolica'])

# --- Plot ---
plt.figure(figsize=(8, 6))

sns.scatterplot(
    x='idade',
    y='pressao_sistolica',
    data=df,
    s=100,
    alpha=0.9,
    edgecolor='black',
    linewidth=0.5
)

plt.title('Gráfico de Dispersão: Idade × Pressão Sistólica', fontsize=14)
plt.xlabel('Idade (anos)', fontsize=12)
plt.ylabel('Pressão Sistólica (mmHg)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
