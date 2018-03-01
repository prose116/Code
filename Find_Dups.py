""" program to combine multiple lists of extensions and then search for
duplicates
Created by Paul Rose Feb 2018"""
import pandas as pd

data = pd.read_csv('removals.csv')

data.columns = ['A']

Ext = list(data.A)
a = len(Ext)

data1 = pd.read_csv('unreg.csv')

# remove .0 from extensions
data1['Ext'] = data1['Ext'].map(lambda x: str(x)[:-2])

Num = list(data1.Ext)
b = len(Num)
new_list = Num + Ext  # combine the 2 lists

c = len(new_list)
print(a, b, c)
my_df = pd.DataFrame(new_list)

my_df.to_csv('Removals.csv', index=False, header=False)

df = pd.read_csv('Removals.csv')
df.columns = ['A']

df['duplicate'] = df.duplicated(['A'])


# We are only interested in the duplicated extensions
df_dup = df.loc[df['duplicate'] == True]


df_dup[df_dup['duplicate']]

print(df_dup)
# Finally let's save our cleaned up data to a csv file
# df_nodup.to_csv('2015sales_nodup.csv', encoding='utf-8')
