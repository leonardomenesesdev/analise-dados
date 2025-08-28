import pandas as pd
import os
print(os.getcwd())
df = pd.read_excel(r"C:\Users\Leonardo\Desktop\analise-dados\database\Mercado.xlsx")
df.head()
print(df.head())
