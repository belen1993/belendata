import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('/home/azureuser/cloudfiles/code/Users/belenolmosvalverde24/belendata/Pandas/titanic.csv')

# Definir los límites de las categorías de edad
bins = [0, 10, 30, 60, 80]
labels = ['0-10', '10-30', '30-60', '60-80']

# Crear una nueva columna con las categorías de edad
df['age_category'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)

# Mostrar las primeras filas del DataFrame para verificar
print(df[['age', 'age_category']].head())