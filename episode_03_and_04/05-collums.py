import pandas as pd

transactions = pd.read_csv("../data/transacoes.csv", sep=";")

print("Tamanho do DF: \n")
print(transactions.shape, "\n")

print("Quanto de memoria ele está usando: \n")
print(transactions.info(memory_usage='deep'), "\n")

print("Tipo de cada coluna: \n")
print(transactions.dtypes)

transactions.rename(columns={"IdTransacao" : "Transacao_id"})
print(transactions.dtypes)

#Select * FROM transactions
print(transactions)

# SELECT IdTransacao, IdCliente FROM transactions
print(transactions[["IdTransacao", "IdCliente"]])