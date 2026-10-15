"""
Predicción de precios de casas con regresión lineal.

Este script carga un conjunto de datos de casas desde un archivo CSV, lo
limpia, entrena un modelo de regresión lineal con scikit-learn y mide su
error al predecir el precio de casas que no vio durante el entrenamiento.

Archivo de entrada
------------------
casas.csv : archivo CSV ubicado en el mismo directorio que el script, con
    las siguientes columnas:

    - metros (int): superficie de la casa en metros cuadrados.
    - habitaciones (int): cantidad de habitaciones.
    - antiguedad (int): antigüedad de la casa en años.
    - precio (int): precio de la casa (variable a predecir).

Flujo del script
----------------
1. Carga el CSV en un DataFrame de pandas.
2. Elimina las filas con datos faltantes (dropna).
3. Separa las variables de entrada (X: metros, habitaciones, antiguedad)
   de la variable objetivo (y: precio).
4. Divide los datos en entrenamiento (80 %) y prueba (20 %). Se usa
   random_state=42 para que la división sea reproducible.
5. Crea y entrena un modelo LinearRegression con los datos de
   entrenamiento.
6. Predice los precios del conjunto de prueba y calcula el error absoluto
   medio (MAE).

Variables principales
---------------------
df : pandas.DataFrame
    Tabla con los datos de las casas (ya sin filas incompletas).
X : pandas.DataFrame
    Features: columnas que el modelo usa para predecir.
y : pandas.Series
    Target: precio real de cada casa.
X_train, X_test : pandas.DataFrame
    Features de entrenamiento y de prueba.
y_train, y_test : pandas.Series
    Precios reales de entrenamiento y de prueba.
modelo : sklearn.linear_model.LinearRegression
    Modelo entrenado. Sus coeficientes quedan en modelo.coef_ y su
    ordenada al origen en modelo.intercept_.
predicciones : numpy.ndarray
    Precios predichos por el modelo para X_test.

Salida
------
Imprime por pantalla el MAE (Mean Absolute Error): el error promedio, en
las mismas unidades que el precio, entre lo que predijo el modelo y el
precio real. Cuanto más bajo, mejor.

Dependencias
------------
pandas, scikit-learn
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# 1. Cargar datos con pandas
df = pd.read_csv("casas.csv")

# 2. Limpiar con pandas
df = df.dropna()   # sacar filas con datos faltantes

# 3. Separar features (X) y target (y)
X = df[["metros", "habitaciones", "antiguedad"]]
y = df["precio"]

# 4. Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Crear y entrenar el modelo (scikit-learn)
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# 6. Predecir y evaluar
predicciones = modelo.predict(X_test)
print(mean_absolute_error(y_test, predicciones))