import warnings  # disable warnings
import pandas as pd  # work data
import matplotlib.pyplot as plt  # work graphics
import numpy as np  # work matrices
import seaborn as sns
import plotly.express as px
import os

path = os.path.dirname(os.path.realpath(__file__))

warnings.filterwarnings('ignore')

print('Script de recomendações')

# configs pandas
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 50)

# configs matplotlib
# size graphic
plt.rcParams['figure.figsize'] = (15, 6)
plt.style.use('seaborn-darkgrid')

# get data
path_books = path + '/tmp/Books.csv'
data_books = pd.read_csv(path_books)

# get ratings
path_ratings = path + '/tmp/Ratings.csv'
data_ratings = pd.read_csv(path_ratings)

# get users
path_users = path + '/tmp/Users.csv'
data_users = pd.read_csv(path_users)
