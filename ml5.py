import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 


df = pd.read_csv("coins.csv" , encoding='ISO-8859-1' , index_col="id")
# coin_name = input("enter the coin name ")
# def_df = df.loc[df['name'] == coin_name]

# def_of_10 = df.loc[df['name'] == coin_name]
# print(def_of_10)


# sns.barplot(x=def_of_10.index , y=def_of_10[['price', 'price_usd', 'totalSupply', 'decimals']])

# sns.relplot(x=def_of_10.index , y=def_of_10['price'] )
# sns.barplot(x=def_of_10.index , y=def_of_10['price_usd'])
# sns.barplot(x=def_of_10.index , y=def_of_10['totalSupply'])
# plt.title('Bar Plot of {} Prices'.format(coin_name))
# plt.xlabel('Column')
# plt.ylabel('Value')

# sns.relplot(x='name' , y='price_usd' , data=def_of_10)
# plt.show()
# sns.barplot(x=def_of_10.index , y=def_of_10.value)
price_zero_usd = len(df.loc[df['price_usd'] == 0])
price_per_usd_low = len(df.loc[df['price_usd'] > 0.0001])
price_Med = len(df.loc[df['price_usd'] > 0.001])
price_high = len(df.loc[df['price_usd'] > 0.01])
data_framefor_count_usd = pd.DataFrame({'price_range':['zero usd ' , 'low usd ' , 'med usd ' , 'high usd'] ,
                                       'Count': [price_zero_usd , price_per_usd_low , price_Med , price_high]}) 
data_framefor_count_usd.to_csv('count_usd_data.csv', index=False)
df2 = pd.read_csv('count_usd_data.csv' , index_col="price_range")
sns.barplot(x=df2.index , y=df2['Count'])
plt.show()

#now plot the same graph for the liquidity 

zero_liquidity = len(df.loc[df['liquidity'] == 0 ])
low_liquidity = len(df.loc[df['liquidity'] > 1.5])
med_liquidity = len(df.loc[df['liquidity'] > 15 ])
high_liquidity = len(df.loc[df['liquidity'] > 20 ])

print(zero_liquidity ,low_liquidity , med_liquidity , high_liquidity )
data_frame_liquidity = pd.DataFrame({'liquidity_range':['zero_li' , 'low_li' , 'med_li' , 'high_li'], 
                                     'CountLiqui': [zero_liquidity , low_liquidity , med_liquidity , high_liquidity]})
data_frame_liquidity.to_csv('coin_liquidity' , index=False)
df3 = pd.read_csv('coin_liquidity' , index_col="liquidity_range")
sns.barplot(x=df3.index , y=df3['CountLiqui'])
plt.show()
# plt.xlabel('Price Range')
# plt.ylabel('Count')
# plt.title('Counts of Coins in Different Price Ranges')
# print(price_zero_usd , "         "  , price_per_usd_low , "     " , price_Med , "     " , price_high )
# plt.figure(figsize=(14,12))
# sns.barplot(x=df.index , y=df['price_usd'])

# plt.show()
# print(df.isnull())