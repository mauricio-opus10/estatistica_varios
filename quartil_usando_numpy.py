# prompt: exemplo de calculo de quartil (primeiro,segundo e terceiro), usando o numpy

import numpy as np

dados = [1000,3000,5000,10000,7000,8000]

# Primeiro quartil (Q1)
primeiro_quartil = np.percentile(dados, 25)
print("Primeiro Quartil (Q1):", primeiro_quartil)

# Segundo quartil (Q2) - equivalente à mediana
segundo_quartil = np.percentile(dados, 50)
print("Segundo Quartil (Q2):", segundo_quartil)

# Terceiro quartil (Q3)
terceiro_quartil = np.percentile(dados, 75)
print("Terceiro Quartil (Q3):", terceiro_quartil)
