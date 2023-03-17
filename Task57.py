# Задача 44: 
# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
#  lst = ['robot'] * 10
#  lst += ['human'] * 10
#  random.shuffle(lst)
#  data = pd.DataFrame({'whoAmI':lst})
#  data.head()



# Visual version :

"""""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI':lst})
unique_vals = data['whoAmI'].unique()

for val in unique_vals:
    data[val] = (data['whoAmI'] == val).astype(int)

data = data.drop('whoAmI', axis=1)

plt.figure(figsize=(6,4))
sns.heatmap(data, cmap='coolwarm', annot=True, fmt='d')
plt.title('One-hot encoding of the whoAmI column')
plt.xlabel('Unique values in the whoAmI column')
plt.ylabel('Rows in the DataFrame')
plt.show()

"""

# Simple version :

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
unique_vals = data['whoAmI'].unique()

for val in unique_vals:
    data[val] = (data['whoAmI'] == val).astype(int)

data = data.drop('whoAmI', axis=1)

data.head()