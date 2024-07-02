import pandas as pd


tabela = pd.read_excel('Vendas.xlsx') # Ler a tabela Excel

faturamento_total = tabela["Valor Final"].sum() #somando a coluna toda do valor final

#faturamento_por_loja = tabela[["ID Loja","Valor Final"]] #aqui ele ta pegando as colunas id loja e valor final , quando voce quer colocar selecionar mais de uma coluna no pandas voce precisa colocar 2 colchetes

faturamento_por_loja = tabela[["ID Loja","Valor Final"]].groupby("ID Loja").sum() # aqui voce ta agrupando as colunas id loja e somando todas as outras colunas 

faturamento_por_produto = tabela[["ID Loja","Produto","Valor Final"]].groupby(["ID Loja","Produto"]).sum() # aqui voce ta agrupando as colunas id loja e produto e depois  somando todas as outras colunas 
print(faturamento_por_loja)