# work data
import pandas as pd

# work matrices
import numpy as np

# work graphics
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# disable warnings
import warnings

warnings.filterwarnings('ignore')

print('Script de recomendações')

# configs pandas
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 50)

# configs matplotlib Z
# size graphic
plt.rcParams['figure.figsize'] = (15, 6)
plt.style.use('seaborn-darkgrid')
