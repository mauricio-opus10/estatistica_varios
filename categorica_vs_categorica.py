from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/USP/datasets/perfil_compras.csv',sep=";")
df.head()
