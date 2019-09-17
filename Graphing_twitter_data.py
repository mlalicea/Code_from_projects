import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def extract(df, characteristics, by_value = False):
    new_df = df
    for key,value in characteristics.items():
        if key in new_df:
            if by_value == False:
                index = value
                new_df = new_df[new_df[key].isin(index)]
                return new_df
            else:
                index = get_valid_index(new_df[key],value)
                new_df = new_df[new_df[key].isin(index)]
                return new_df

def get_valid_index(ser,cutoff):
    v = ser.value_counts()
    return list(v[v>=cutoff].index)

def compare_bar(df, plot_cat, hue_cat, log = False, rotation = 0, dim = [8,8], legend_loc = 'best'):
    plt.figure(figsize = dim)
    plt.xticks(rotation = rotation)
    if log == True:
        plt.yscale('log')
    graph = sns.countplot(df[plot_cat], hue = df[hue_cat])
    plt.legend(loc = legend_loc, title = hue_cat)
    return graph

def compare_heat(df, cat_1, cat_2, norm = False, dim = [10,10]):
    table = pd.crosstab(df[cat_1], df[cat_2], normalize=norm)
    plt.figure(figsize = dim)
    heat = sns.heatmap(table)
    return heat

if __name__ == '__main__':
    #Read in data
    alln = pd.read_csv('twitter_meta.csv')
    #Remove any rows where post_type is marked as retweet or quote_tweet
    alln = alln[(alln.post_type != 'RETWEET') & (alln.post_type != 'QUOTE_TWEET')]
    #Remove post_type, account_category, updates columns
    alln = alln.drop(['post_type', 'account_category', 'updates'],axis = 1)
    #Check for missing values
    print(alln.isnull().sum())
    #Replace LANGUAGE UNDEFINED and Unknown with nan for the language column ONLY
    alln.language.replace(['LANGUAGE UNDEFINED', 'Unknown'], np.nan, inplace = True)
    #Put account_type in all caps
    alln['account_type'] = alln['account_type'].str.upper()
    #Use a dictionary to update/correct some language names
    replacements = {'Pushto':'Pashto', 'Farsi (Persian)': 'Farsi', 'Tagalog (Filipino)':'Tagalog'}
    alln['language'] = alln['language'].apply(lambda x: (replacements.get(x, x)))
    #Check for missing values
    print(alln.isnull().sum())
    #Drop any rows with missing data
    alln = alln.dropna()

	#Write your main program here:
print(extract(alln, {'language':['Greek']}, by_value = False))
left_right = extract(alln, {'account_type':['LEFT', 'RIGHT']}, by_value = False)
for_graph = extract(left_right, {'language':10}, by_value = True)
compare_bar(for_graph, 'language', 'account_type', log = True, rotation = 90, dim = [8,8], legend_loc = 'best')
for_heat = extract(alln, {'language':100, 'region':100}, by_value = True)
compare_heat(for_heat, 'language', 'region', norm = 'index', dim = [10,10])
compare_heat(for_heat, 'language', 'region', norm = 'columns', dim = [10,10])
