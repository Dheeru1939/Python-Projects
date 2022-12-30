import pandas as pd
import numpy as np
import re

df=pd.read_csv('omicron.csv')
print('Code being developed by 202204104610033')

df=df.dropna()
str1=" "

namelist=list(map(lambda x:re.findall('[a-zA-Z,]+',x),df['user_location']))

name=list(map(lambda x:str1.join(x),namelist))

print(df['user_location'])
df['user_location']=name
print(df['user_location'])

# print('Q1')
# df_to_list=df.values.tolist()
# df_to_numarray=df.to_numpy()

# print(type(df_to_list))
# print(type(df_to_numarray))

# print('Q2')
# print(df.loc[df['user_followers']==max(df['user_followers']),['user_name','user_location','user_followers']])

# print('Q3')
# print(df.loc[df['user_location']=='United Kingdom',['text','user_location']])

# print('Q4')
# print(df.groupby('user_location')['user_name'].nunique())

# print('Q5')
# print(df.groupby('user_location').agg(Max_Friends=('user_friends',np.max)))

# print('Q6')
# print(df.groupby('user_location').agg(Avg_Tweets=('retweets',np.average)))

# print('Q7')
# print('Median of user friends',np.median(df['user_friends']))
# print('Mode of user friends',df['user_friends'].mode())

# print('Median of user followers',np.median(df['user_followers']))
# print('Mode of user followers',df['user_followers'].mode())

# print('Q8')
# print(zip(df.groupby('user_name')['retweets'].sum().where(lambda x:x>300).dropna()))

# print('Q9')
# print(df.sort_values(by=['retweets'],ascending=False).head())

# print('Q10')
# df['hashtags']=df['hashtags'].fillna('[]')
# print(df.loc[df['hashtags'].apply(lambda x:'Omicron' in x),['text','hashtags']])

# print('Q11')
# print(df.loc[df['source'].str.contains('iPhone|Android'),['source']])

# print('Q12')
# print(df.loc[df['user_verified']==True,['text','user_verified']])

# print('Q13')
# df['date']=pd.to_datetime(df['user_created']).dt.date

# #All day tweet data
# df.groupby('date')['text'].count()

# #Canada tweet data

# df.loc[df['user_location']=='Canada'].groupby('date')['text'].count()



# print('Q14')
# print(df.loc[df['text'].str.contains('COVID'),['text']])

# print('Q15')

# IndiaLocation = {'location': ['Mumbai', 'Gurgaon', 'Bangalore', 'New Delhi'],
# 'tweets': [23845, 171995, 135925 , 71400]}

# USLocation = {'location': ['Wisconsin', 'West Virginia', 'Ohaio', 'California'],
# 'tweets': [29995, 23600, 61500 , 58900]}

# dfIndianLocation=pd.DataFrame(IndiaLocation)
# dfUSLocation=pd.DataFrame(USLocation)

# print(pd.concat([dfIndianLocation,dfUSLocation],keys=['India','United States'],axis=0))

# print('Q16')
# Loc_retweets = {'location': ['Mumbai', 'Gurgaon', 'Bangalore', 'New Delhi'],
# 'retweets': [23845, 17995, 135925 , 71400]}
# Loc_favorites = {'location': ['Mumbai', 'Gurgaon', 'Bangalore', 'New Delhi'],
# 'favorites': [141, 80, 182 , 160]}

# dfLoc_retweets=pd.DataFrame(Loc_retweets)
# dfLoc_favorites=pd.DataFrame(Loc_favorites)

# print(pd.merge(dfLoc_retweets,dfLoc_favorites))
