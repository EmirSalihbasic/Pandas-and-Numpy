# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 12:35:56 2023

@author: Korisnik
"""

#import pandas
import pandas as pd


# =============================================================================
#                              DATAFRAMES
# =============================================================================


# create an empty dataframe
df = pd.DataFrame()
df

# create dataframe from a list
data = [10,20,30,40,50,60]
df = pd.DataFrame(data)
df

# create dataframe from a list and name the column
data = [10,20,30,40,50,60]
df = pd.DataFrame(data, columns=['Numbers'])
df

# create dataframe from list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
df

# create dataframe with dictionary
data = {'Name': ['Tom', 'nick', 'krish', 'jack'],
        'Age': [20, 21, 19, 18]}
df = pd.DataFrame(data)
df

#create dataframe with index labels #indexes are rank1, rank2, rank 3...
data = {'Name': ['Tom', 'Jack', 'nick', 'juli'],
        'marks': [99, 98, 95, 90]}
df = pd.DataFrame(data, index=['rank1',
                               'rank2',
                               'rank3',
                               'rank4'])
df

# =============================================================================
#                               JOINS IN PANDAS
# =============================================================================

#dataframe a
a = pd.DataFrame()
d = {'name': ['Michael', 'George', 'Caroline', 'Elizabeth'],
     'salary': [1800, 1600, 2000, 1500]}
a = pd.DataFrame(d)
a

#dataframe b

b = pd.DataFrame()

d = {'name': ['Michael', 'Robert', 'Caroline', 'Eleanor'],
     'city': ['New York', 'Chicago', 'Los Angeles', 'Houston']}
b = pd.DataFrame(d)
b

#inner join with these two dataframes

a = pd.DataFrame()
d = {'name': ['Michael', 'George', 'Caroline', 'Elizabeth'],
     'salary': [1800, 1600, 2000, 1500]}
a = pd.DataFrame(d)

b = pd.DataFrame()

d = {'name': ['Michael', 'Robert', 'Caroline', 'Eleanor'],
     'city': ['New York', 'Chicago', 'Los Angeles', 'Houston']}
b = pd.DataFrame(d)
 

df = pd.merge(a, b, on='name', how='inner')   # only this command is for inner join
df

#left outer join

a = pd.DataFrame()
d = {'name': ['Michael', 'George', 'Caroline', 'Elizabeth'],
     'salary': [1800, 1600, 2000, 1500]}
a = pd.DataFrame(d)

b = pd.DataFrame()

d = {'name': ['Michael', 'Robert', 'Caroline', 'Eleanor'],
     'city': ['New York', 'Chicago', 'Los Angeles', 'Houston']}
b = pd.DataFrame(d)


df = pd.merge(a, b, on='name', how='left') #only this command is for join

df

#right outer join

a = pd.DataFrame()
d = {'name': ['Michael', 'George', 'Caroline', 'Elizabeth'],
     'salary': [1800, 1600, 2000, 1500]}
a = pd.DataFrame(d)

b = pd.DataFrame()

d = {'name': ['Michael', 'Robert', 'Caroline', 'Eleanor'],
     'city': ['New York', 'Chicago', 'Los Angeles', 'Houston']}
b = pd.DataFrame(d)


df = pd.merge(a, b, on='name', how='right')

df

#full outer join
a = pd.DataFrame()
d = {'name': ['Michael', 'George', 'Caroline', 'Elizabeth'],
     'salary': [1800, 1600, 2000, 1500]}
a = pd.DataFrame(d)

b = pd.DataFrame()

d = {'name': ['Michael', 'Robert', 'Caroline', 'Eleanor'],
     'city': ['New York', 'Chicago', 'Los Angeles', 'Houston']}
b = pd.DataFrame(d)
df = pd.merge(a, b, on='name', how='outer')
df
              
#index outer join
a = pd.DataFrame()
d = {'name': ['Michael', 'George', 'Caroline', 'Elizabeth'],
     'salary': [1800, 1600, 2000, 1500]}
a = pd.DataFrame(d)

b = pd.DataFrame()

d = {'name': ['Michael', 'Robert', 'Caroline', 'Eleanor'],
     'city': ['New York', 'Chicago', 'Los Angeles', 'Houston']}
b = pd.DataFrame(d)

df = pd.merge(a, b, left_index=True, right_index=True)             
df
              
# =============================================================================
#                                    IMPORT A FILE
# =============================================================================

#csv
import pandas as pd

df = pd.read_csv(r'C:/Users/Korisnik/Desktop/csv.import.csv')
print(df)

#excel
import pandas as pd

df = pd.read_excel('C:/Users/Korisnik/Desktop/excel.import.xlsx')

print(df)


