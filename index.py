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

# lines and columns
# print(data_books.shape)
# print(data_ratings.shape)
# print(data_users.shape)

# firsts lines books
firsts_books = data_books.head()
# print(firsts_books)

# info header books
info_books = data_books.info()
# print(info_books)

# join datas

# join books with ratings
join_books_with_ratings = data_books.merge(data_ratings, how='inner', on='ISBN')

# join books_ratings with users
join_books_with_users = join_books_with_ratings.merge(data_users, how='inner', on='User-ID')

join_books_with_users.info()
# join_books_with_users.head()
