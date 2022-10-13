import warnings  # disable warnings
import pandas as pd  # work data
import matplotlib.pyplot as plt  # work graphics
import numpy as np  # work matrices
import seaborn as sns
import plotly.express as px
import os

warnings.filterwarnings('ignore')


# split string
def explode(region):
    region_arr = region.split(',')
    country = region_arr[-1].upper()

    ret = country

    return ret


def load_file(file_name):
    path = os.path.dirname(os.path.realpath(__file__))
    path_file = path + '/tmp/' + file_name

    data = pd.read_csv(path_file)

    return data


print('Script de recomendações')

# configs pandas
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 50)

# configs matplotlib
# size graphic
plt.rcParams['figure.figsize'] = (15, 6)
plt.style.use('seaborn-darkgrid')

########################################### Importação dos dados

# get datas
data_books = load_file('Books.csv')
data_ratings = load_file('Ratings.csv')
data_users = load_file('Users.csv')

########################################### Modelagem dos dados

# join datas
join_books_with_ratings = data_books.merge(data_ratings, how='inner', on='ISBN')
join_books_with_users = join_books_with_ratings.merge(data_users, how='inner', on='User-ID')

# incorret resgitry
join_books_with_users.iloc[287500, 3] = ''
join_books_with_users.iloc[352361, 3] = ''
join_books_with_users.iloc[467962, 3] = ''
join_books_with_users.iloc[469216, 3] = ''

# convert column year
join_books_with_users['Year-Of-Publication'] = pd.to_numeric(join_books_with_users['Year-Of-Publication'])

# select locarions colunm
locations = join_books_with_users['Location']

# new colunn country
join_books_with_users['country'] = locations.apply(explode)

########################################### Data Visualization - Exploration

data_describe = join_books_with_users.describe()
print(data_describe)
