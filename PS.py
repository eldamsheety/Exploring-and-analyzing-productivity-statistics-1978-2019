import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('productivity-statistics-1978-2019-csv.csv')

df.head()
df.shape
df.info()
df.describe()
