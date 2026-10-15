import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
n = 500

metros = rng.integers(30, 160, n)
habitaciones = np.clip(metros // 30 + rng.integers(-1, 2, n), 1, 5)
antiguedad = rng.integers(0, 40, n)

precio = (
    1500 * metros
    + 8000 * habitaciones
    - 500 * antiguedad
    + rng.normal(0, 8000, n)   # ruido, para que no sea perfecto
).round(-3)

df = pd.DataFrame({
    "metros": metros,
    "habitaciones": habitaciones,
    "antiguedad": antiguedad,
    "precio": precio.astype(int),
})

# Meter algunos vacíos para practicar dropna()
df.loc[rng.choice(n, 10, replace=False), "antiguedad"] = np.nan

df.to_csv("casas.csv", index=False)
print(df.head())