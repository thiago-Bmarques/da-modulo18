import pandas as pd

# Carregar o arquivo CSV em um DataFrame
df_galosina = pd.read_csv('gasolina.csv')

import seaborn as sns

#gerar grágico
with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data= df_galosina, x = 'dia', y = 'venda', palette='pastel')
  grafico.set(title = 'Preço da gasolina', xlabel = 'dia', ylabel = 'venda');

#salvar imagem
  grafico.figure.savefig("gasolina.png")