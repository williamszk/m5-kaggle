

import pandas as pd

df = pd.read_csv('C://Users//cacal//Downloads//sell_prices.csv', sep = ',')
df2 = pd.read_csv('C://Users//cacal//Downloads//calendar.csv', sep = ',')
print(len(df))
df3 = df.iloc[0:3000000,:]
df4 = df.iloc[3000001:-1,:]

df_final = pd.merge(df3,
                 df2,
                 left_on='wm_yr_wk', 
                 right_on='wm_yr_wk',
                 how = "inner")

df_final2 = pd.merge(df4,
                 df2,
                 left_on='wm_yr_wk', 
                 right_on='wm_yr_wk',
                 how = "inner")

print(len(df_final))
print(len(df_final2))

df_final.drop_duplicates( inplace = True)
df_final2.drop_duplicates( inplace = True)

print(len(df_final))
print(len(df_final2))


df_final3 = df_final.append(df_final2) 
print(df_final3.head())
print(len(df_final3))
df_final3.drop_duplicates( inplace = True)
print(len(df_final3)) 
  

compression_opts = { 'method' : 'zip', 'archive_name' : 'df_final3.csv'}

df_final2.to_csv('df_final2.csv')