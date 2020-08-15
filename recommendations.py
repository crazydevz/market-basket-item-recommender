import pandas as pd

# saved_rules = pd.read_excel('rules.xlsx', dtype={'consequents':str})

country_name = input('Enter your country name: ')

item_name = input('Enter the item name: ')

saved_rules = pd.read_excel('rules-for-' + country_name +'.xlsx')

resultants = saved_rules[ (saved_rules['antecedents'].astype('str').str.contains(item_name)) ]

if(resultants.empty == False):
    print(resultants['consequents'])
else:
    print('Sorry, no recommendations for this item')