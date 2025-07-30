import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")
# print("Esses são os 10 primeiros registros")
# print(df_clientes.head(10), "\n")

# print("Esses são os 10 ultimos registros")
# print(df_clientes.tail(10), "\n")

# print("Esses é uma amostra aléatoria de 10 registros")
# print(df_clientes.sample(10), "\n")
print(df_clientes.info())