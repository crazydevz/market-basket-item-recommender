import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

def generateRulesForCountry(country_name, min_support):
    df = pd.read_excel('Online_Retail.xlsx')

    df['Description'] = df['Description'].str.strip()
    df.dropna(axis=0, subset=['InvoiceNo'], inplace=True)
    df['InvoiceNo'] = df['InvoiceNo'].astype('str')
    df = df[~df['InvoiceNo'].str.contains('C')]

    basket = (df[df['Country'] == country_name]
        .groupby(['InvoiceNo', 'Description'])['Quantity']
        .sum().unstack().reset_index().fillna(0)
        .set_index('InvoiceNo'))

    def encode_units(x):
        if x <= 0:
            return 0
        if x >= 1:
            return 1
    basket_sets = basket.applymap(encode_units)
    basket_sets.drop('POSTAGE', inplace=True, axis=1)

    frequent_itemsets = apriori(basket_sets, min_support, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

    if(rules.empty):
        print('Rules at min_support ' + str(min_support) + ' are not available for this country!. Please reduce the min_support value as this country seems to have little or few association rules')
        return

    # Saving the generated rules
    rules[(rules['lift'] >= 6) &
    (rules['confidence'] >= 0.8)].to_excel('rules-for-' + country_name +'.xlsx')

country_name = input("Enter your country name: ")
min_support = float(input("Enter min_support: "))

if(country_name and min_support):
    print("Generating Association Rules... This may take a moment.")

generateRulesForCountry(country_name, min_support)