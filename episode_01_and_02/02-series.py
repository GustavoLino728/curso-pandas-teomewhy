import pandas as pd

# Series é meio tipada, ela aceita outros tipos de dados mas converte pra o que for a maioria
num = [89, 123, 10, 92, 252, 25, 25, 18, 1230]
names = ['Gustavo', 'Gustavo Lino', 'Gustavo', 'Paulo', 'Juninho']

age_series = pd.Series(names)
print(age_series.mean())