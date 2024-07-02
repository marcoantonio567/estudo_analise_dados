import pandas as pd
import plotly.express as px

tabela = pd.read_csv("planilhas/ClientesBanco.csv", encoding="latin1")
tabela = tabela.drop("CLIENTNUM", axis=1)#aqui eu to excluindo uma coluna esse parametro de eixo sigifica 0 para linha e 1 para coluna
tabela = tabela.drop("Educação", axis=1)
tabela = tabela.dropna()#aqui ele excluindo todos os valores vazios na tabela 
# print(tabela.info())#aqui ele vai rodar umas informações sobre a sua tablea 
#print(tabela.describe().round(1))#nesse discribe ele mostra :quantos itens temos , media , desvio padrão , minimo , 25%,50%,75% pra baixo e o maximo , nessa ordem //so funciona em colunas de numeros

qtde_cartegoria = tabela["Categoria"].value_counts()#aqui ele ta te dando um numero absoluto das suas catergorias quantos foram cancelados e quantos são clientes
# print(qtde_cartegoria)
qtde_cartegoria = tabela["Categoria"].value_counts(normalize=True)#aqui ele ta te dando um percentual das suas catergorias quantos foram cancelados e quantos são clientes
# print(qtde_cartegoria)
for coluna in tabela:
    grafico = px.histogram(tabela,x=coluna,color="Categoria")
    grafico.show()