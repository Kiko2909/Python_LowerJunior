#Задача 42: 
#Узнать какая максимальная households в зоне минимального значения population

import pandas as pd

data = pd.read_csv('california_housing_test.csv')
min_pop_row = data.loc[data['population'].idxmin()]
households = min_pop_row['households']
max_households = data.loc[(data['latitude'] == min_pop_row['latitude']) 
                          & (data['longitude'] == min_pop_row['longitude']), 'households'].max()

print("The maximum households in the zone of the minimum population value is:", max_households)