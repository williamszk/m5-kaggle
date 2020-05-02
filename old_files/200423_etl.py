
import numpy as np
import pandas as pd


project_path = "C:\\Projects\\m5-kaggle\\" 
####################################################################
sales_path = project_path+"m5-forecasting-accuracy\\sales_train_validation.csv"
sales = pd.read_csv(sales_path)

#We need to transpose sales so that each line is a day and each column is a 
#produc/store. This new data frame will have 1913 rows and 30490 columns.

#Each column d_ is a day. There are 1913 days in our base. And 30490 products/stores.

#delete some variables
sal2 = sales.drop(['item_id','dept_id','cat_id','store_id','state_id'],axis=1)

#take the name of id and erase _validation from it
def ex_val(word):
    new_word = word[0:(len(word)-11) ]
    return new_word
new_id = [ex_val(word) for word in sal2['id']]

#replace the old variable
sal2['id'] = new_id

sal2.head()

#transpose the data frame
sal3 = sal2.T

#the first line of the data frame are the names of product/location
#lets drop it
sal4 = sal3.drop(['id'],axis=0).copy()

#change the column names of sal4
sal4.columns = sal3.iloc[0,:]

#finished preparing sales dataset
#=========================
sell_prices = project_path+"m5-forecasting-accuracy\\sell_prices.csv"
prices = pd.read_csv(sell_prices)

prices.head()
prices.shape
prices["wm_yr_wk"].value_counts()

#transpose prices data frame 
#columns are products/places
#lines are date identifiers

#create a single variable for store_id and item_id
item_store = prices["item_id"]+"_"+prices["store_id"]

prices2 = prices.drop(['store_id', 'item_id'], axis=1)
prices2["item_store"] = item_store

prices3 = prices2.pivot(index='wm_yr_wk', columns='item_store', values='sell_price')

#reset index and wm_yr_wk becomes a column
prices4 = prices3.reset_index().copy()

#finished preparing prices

#===========================================
calendar_path = project_path+"m5-forecasting-accuracy\\calendar.csv"
calendar = pd.read_csv(calendar_path)

calendar.head().iloc[0:5,0:4]

#each line of this data set is a day and it lists the events
#for each location, for example it lists if there was a holyday etc...

#we can enrich this dataset with prices4 data frame 
#merge calendar with prices4
prCal = calendar.merge(prices4,left_on='wm_yr_wk',right_on='wm_yr_wk',how='left')

#--
prCal.shape
Out[39]: (1969, 30504)
#each line of prCal is a day
#the columns are prices for all products/locations
#there are three columns for events
#price change weekly...


#===============================================

######################################################
#there are 10 different regions or locations
CA_1
CA_2
CA_3
CA_4
TX_1
TX_2
TX_3
WI_1
WI_2
WI_3

#there are 3049 different products...
HOUSEHOLD_1_389    2820
HOBBIES_1_341      2820
HOUSEHOLD_1_368    2820
HOBBIES_1_301      2820
HOUSEHOLD_2_299    2820
...
HOUSEHOLD_1_308     642
HOUSEHOLD_1_159     623
HOUSEHOLD_1_242     600
FOODS_3_296         592
FOODS_2_379         530
Name: item_id, Length: 3049, dtype: int64
######################################################















































