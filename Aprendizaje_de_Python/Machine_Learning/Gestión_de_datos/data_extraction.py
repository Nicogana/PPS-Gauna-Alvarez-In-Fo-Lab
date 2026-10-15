import pandas as pd


# df = DataFrame
df = pd.read_csv(r'C:\Users\alvar\Info-Lab\Machine_Learning\abalone.data', header=None, names=['Sex', 'Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings'])
#for index, row in data.iterrows():
   # print(row)

#print(df.to_string())
#df.to_csv(r'C:\Users\alvar\Info-Lab\Machine_Learning\abalone.csv')
#df.info()
#print(df.describe().to_string())
dfj = pd.read_json(r'C:\Users\alvar\Info-Lab\Machine_Learning\data.json')
#dfj.info()
print(dfj.loc[168])
#print(dfj.to_string())
#dfj.to_csv(r'C:\Users\alvar\Info-Lab\Machine_Learning\data.csv')

# existen 2 tipos de busquedas por indice: loc (nro de columna) y iloc (nro de fila)