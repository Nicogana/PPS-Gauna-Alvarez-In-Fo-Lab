import pandas as pd

df = pd.read_csv(r'C:\Users\alvar\Info-Lab\Machine_Learning\countries.csv')
##print(df.loc['Albania'])
#print()
#print(df.iloc[2])

#df.reset_index()
df['Region'] = df['Region'].str.strip()
df['Country'] = df['Country'].str.strip()

df.set_index(['Region', 'Country'], inplace=True)
df.sort_index(inplace=True)
#print(df.loc['EASTERN EUROPE', 'Bulgaria'])
# iloc es estrictamente posicional, en un DF que tiene mas de 1 nivel, 
# indexa por la primera columna por la cual puede diferenciar cada uno de los datos.
# En este caso la primera columna es Region, pero esta se repite, 
# por lo que indexa por la 2da columna (Country), ya que es la primera
# columna que identifica univocamente a cada fila
print(df.iloc[2])
#df.to_csv(r'C:\Users\alvar\Info-Lab\Machine_Learning\country_data.csv') 
