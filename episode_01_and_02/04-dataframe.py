import pandas as pd

ages = [
    10,20,30,40,50,60,70,100,98
]

nomes = ['Gustavo', 'Lino', 'de Araújo', 'Carlos', 'ABC', 'A', 'G', 'L', 'g']

ages = pd.Series(ages)
age_frame = pd.DataFrame(ages)
age_frame["ages"] = ages

age_frame["nomes"] = nomes


print(age_frame.iloc[::-1])
print(age_frame.iloc[0]["ages"])
pd.read_excel