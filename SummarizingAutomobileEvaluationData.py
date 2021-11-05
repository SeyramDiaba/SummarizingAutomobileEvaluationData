import pandas as pd
import numpy as np

car_eval = pd.read_csv('car_eval_dataset.csv')
print('-------------------------------------')
print(car_eval.head())
print('-------------------------------------')

# Modal summary of 'manufacturer_country'
mode_freq = car_eval['manufacturer_country'].value_counts()
print(mode_freq)
print('The 4th most frequent country is ',"''",mode_freq.index[3],"''")
print('-------------------------------------')

# Table of proportions for countries that appear in manufacturer_country
prop_countries = car_eval['manufacturer_country'].value_counts(normalize = True)
print(prop_countries)
print('-------------------------------------')
print(prop_countries[0]*100,'% of cars were manufactured in Japan.')
print('-------------------------------------')

# List of unique values in 'buying_cost' variable
print(car_eval['buying_cost'].unique())

# New list of unique values in 'buying_cost' from lowert to highest
buying_cost_categories = ['low','med','high','vhigh']

# Converting buying_cost to category type using 'buying_cost_categories'
car_eval['buying_cost'] = pd.Categorical(car_eval['buying_cost'], buying_cost_categories, ordered = True)

# Calculated the median category of 'buying_cost'
buying_cost_median_ind = np.median(car_eval['buying_cost'].cat.codes)
buying_cost_median = buying_cost_categories[int(buying_cost_median_ind)]
print('The median is: ',buying_cost_median)

# Table of proportions for 'luggage' variable
luggage_prop = car_eval['luggage'].value_counts(normalize = True)
print('Luggage proportions:\n',luggage_prop)

# Table of proportions for 'luggage' variable including missing values
luggage_prop_missing = car_eval['luggage'].value_counts(normalize = True, dropna= False)
print('-------------------------------------')
print("luggage proportions including missing fields: \n",luggage_prop_missing) # There are no missing values
print('-------------------------------------')

# Achieving proportion without passing the 'normalize' argument
test_luggage_prop = car_eval['luggage'].value_counts()/len(car_eval['luggage'])
print("luggage proportions test without the 'normalize' argument: \n",test_luggage_prop)
print('-------------------------------------')
# Summarising passenger Capacity with 'door' variable.
passenger_summary = np.sum(car_eval['doors'] == '5more')
print('Number of cars with 5+ doors: ',passenger_summary)

#Proportion of cars that have 5+ doors
five_plus_doors_prop = np.mean(car_eval['doors'] == '5more')
print('-------------------------------------')
print('Proportion of cars with 5+ doors: ',five_plus_doors_prop)
