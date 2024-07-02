import plotly.express as px


# # criando dados

dados_x = ["2018","2019","2020","2021"]
dados_y = [10,20,5,35]

# # criando uma variavel que vai receber esse seu grafico

fig = px.line(x=dados_x, y=dados_y , title="vendas ano" , width=600, height=300)#aqui ele ta criando um grafico de linha , coloando um titulo uma algura e uma largura espeficia
fig.update_yaxes(title="vendas", title_font_color="red")#alterando o nome y e colocando ele vermelho
fig.update_xaxes(title="vendas1", title_font_color="blue")#alterando o nome x e colocando ele azul

fig = px.pie(names=dados_x, values=dados_y , title="vendas ano" , width=600, height=300)#aqui ele ta colocando um grafico de pizza e definindo seu tamanho
# fig.show()#aqui ele ta mostrando o grafico 

##############grafico de dispersão#############

import plotly.graph_objects as go

# Dados
x = [1, 2, 3, 4, 5]
y = [10, 11, 12, 13, 14]

# Criando o gráfico
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers'))

# Personalizando o layout
fig.update_layout(title='Gráfico de Dispersão',
                  xaxis_title='Eixo X',
                  yaxis_title='Eixo Y')


#graficos de barras

import plotly.graph_objects as go

# Dados
x = ['A', 'B', 'C', 'D']
y = [10, 20, 15, 25]

# Criando o gráfico
fig = go.Figure(data=[go.Bar(x=x, y=y)])

# Personalizando o layout
fig.update_layout(title='Gráfico de Barras',
                  xaxis_title='Categorias',
                  yaxis_title='Valores')


#grafico de pizza 
import plotly.graph_objects as go

# Dados
labels = ['A', 'B', 'C', 'D']
values = [30, 20, 15, 35]

# Criando o gráfico
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

# Personalizando o layout
fig.update_layout(title='Gráfico de Pizza')

#
