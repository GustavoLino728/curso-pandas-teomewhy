import pandas as pd

CSV_PATH = "../data/clientes.csv"

df = pd.read_csv(CSV_PATH)

df.to_excel("teste.xlsx", sep=";")