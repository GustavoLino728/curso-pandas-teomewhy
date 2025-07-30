import pandas as pd

url = "https://www.w3schools.com/html/html_tables.asp"

# Retorna uma lista de tabelas encontradas na URL
notion_table = pd.read_html(url)

example_table = notion_table[0]
print(example_table)

# Filtrando
germany = example_table[example_table["Country"] == "Germany"]
print(germany)
